// 語言切換：?lang= → 上次選的 → 裝置語言；沒有 JS 時預設繁中
(function(){
  var OK=['zh-Hant','en','ja'],K='ember-site-lang',root=document.documentElement;
  function pick(){
    var q=(location.search.match(/[?&]lang=([^&]+)/)||[])[1];if(q&&OK.indexOf(q)>=0)return q;
    try{var s=localStorage.getItem(K);if(s&&OK.indexOf(s)>=0)return s}catch(e){}
    var ls=navigator.languages||[navigator.language||''];
    for(var i=0;i<ls.length;i++){var l=String(ls[i]).toLowerCase();if(/^zh/.test(l))return 'zh-Hant';if(/^ja/.test(l))return 'ja';if(/^en/.test(l))return 'en'}
    return 'en'}
  function set(l){root.setAttribute('data-lang',l);root.lang=l;
    var bs=document.querySelectorAll('.langs button');for(var i=0;i<bs.length;i++)bs[i].setAttribute('aria-pressed',bs[i].getAttribute('data-set')===l?'true':'false');
    var t=document.querySelector('meta[name="title-'+l+'"]');if(t)document.title=t.content}
  set(pick());
  document.addEventListener('DOMContentLoaded',function(){set(root.getAttribute('data-lang'));
    var bs=document.querySelectorAll('.langs button');for(var i=0;i<bs.length;i++)bs[i].addEventListener('click',function(){var l=this.getAttribute('data-set');try{localStorage.setItem(K,l)}catch(e){}set(l)})});
})();
