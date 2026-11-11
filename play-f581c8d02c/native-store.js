/* 燼燈深淵：App 版的存檔備份（網頁版沒有 Capacitor，這個檔案什麼都不做）
 *
 * 遊戲照樣用 localStorage 同步讀寫（快、簡單）。這裡做兩件事：
 * 1. 每次寫入或刪除 ember-abyss-* 的資料，同時寫進 App 原生的儲存空間（Capacitor Preferences）。
 *    iOS 在空間不足時可能清掉 App 內網頁的資料，但不會清掉原生儲存。
 * 2. App 啟動時比對：原生備份有、網頁儲存卻沒有的資料，就還原回去並重新載入一次。
 *    第一次裝了這個版本時，反方向把現有的網頁資料補進原生備份。
 *
 * 刪除也會同步（例如角色死亡刪掉存檔），所以不會因為還原而讓死掉的角色復活。
 * 必須在遊戲主程式之前載入。
 */
(function(){
  'use strict';
  var Pref=window.Capacitor&&window.Capacitor.Plugins&&window.Capacitor.Plugins.Preferences;
  if(!Pref)return;
  var PREFIX='ember-abyss',ls;
  try{ls=window.localStorage}catch(e){return}
  var mine=function(k){return typeof k==='string'&&k.indexOf(PREFIX)===0};
  // 載入當下網頁儲存裡本來有哪些鍵（之後遊戲新建的不算）
  var initial={};try{for(var j=0;j<ls.length;j++){var kk=ls.key(j);if(mine(kk))initial[kk]=1}}catch(e){}
  var quiet=function(p){if(p&&p.catch)p.catch(function(){})};
  // 啟動比對完成前的寫入先排隊，免得一筆新的空資料蓋掉原生備份
  var ready=false,queue={};
  var push=function(k,v){if(!ready){queue[k]=v;return}if(v===null)quiet(Pref.remove({key:k}));else quiet(Pref.set({key:k,value:v}))};

  // 1. 鏡像寫入：攔下 Storage 的 setItem／removeItem（只處理 localStorage 上本遊戲的鍵）
  var S=Storage.prototype,origSet=S.setItem,origRemove=S.removeItem;
  S.setItem=function(k,v){origSet.call(this,k,v);if(this===ls&&mine(k))push(k,String(v))};
  S.removeItem=function(k){origRemove.call(this,k);if(this===ls&&mine(k))push(k,null)};
  var flush=function(){ready=true;for(var k in queue)push(k,queue[k]);queue={}};

  // 2. 啟動時比對兩邊
  var FLAG='ember-abyss-restored';
  Pref.keys().then(function(r){
    var keys=(r&&r.keys||[]).filter(mine),have={},restore=[];
    keys.forEach(function(k){have[k]=1;if(!initial[k])restore.push(k)});
    // 原生備份沒有、網頁有的 → 補進備份（第一次升級到這個版本時）
    for(var i=0;i<ls.length;i++){var k=ls.key(i);if(mine(k)&&initial[k]&&!have[k]&&!(k in queue))quiet(Pref.set({key:k,value:ls.getItem(k)}))}
    if(!restore.length){flush();return}
    // 同一次啟動只還原一次，避免任何意外造成重新載入的迴圈
    var once=null;try{once=sessionStorage.getItem(FLAG)}catch(e){}
    if(once){flush();return}
    return Promise.all(restore.map(function(k){return Pref.get({key:k}).then(function(g){if(g&&g.value!=null)origSet.call(ls,k,g.value)})}))
      .then(function(){try{sessionStorage.setItem(FLAG,'1')}catch(e){}location.reload()});
  }).catch(flush);
})();
