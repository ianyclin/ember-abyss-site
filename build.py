# 產生網站三頁：python3 build.py
import os
D = os.path.dirname(os.path.abspath(__file__))
MAIL = 'hello@sanbaofang.com'
TITLES = {'index': {'zh-Hant': '燼燈深淵 Emberlamp Abyss', 'en': 'Emberlamp Abyss', 'ja': '燼燈深淵 Emberlamp Abyss'},
          'support': {'zh-Hant': '技術支援・燼燈深淵', 'en': 'Support · Emberlamp Abyss', 'ja': 'サポート・燼燈深淵'},
          'privacy': {'zh-Hant': '隱私權政策・燼燈深淵', 'en': 'Privacy Policy · Emberlamp Abyss', 'ja': 'プライバシーポリシー・燼燈深淵'}}
DESC = '提一盞燈，走下十層地窟。燈油燒乾，黑暗就會進食。Carry a lamp ten floors down. When the oil runs dry, the dark feeds.'
NAV = {'zh-Hant': ('首頁', '技術支援', '隱私權政策'), 'en': ('Home', 'Support', 'Privacy'), 'ja': ('ホーム', 'サポート', 'プライバシー')}

def L(zh, en, ja, tag='span'):
    return f'<{tag} data-l="zh-Hant">{zh}</{tag}><{tag} data-l="en">{en}</{tag}><{tag} data-l="ja">{ja}</{tag}>'

def page(name, body, up):
    t = TITLES[name]
    navl = lambda i, href: f'<a href="{up}{href}"{" aria-current=\"page\"" if (name, i) in (("index", 0), ("support", 1), ("privacy", 2)) else ""}>{L(*[NAV[l][i] for l in ("zh-Hant", "en", "ja")])}</a>'
    return f'''<!doctype html>
<html lang="zh-Hant" data-lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{t["zh-Hant"]}</title>
<meta name="title-zh-Hant" content="{t["zh-Hant"]}"><meta name="title-en" content="{t["en"]}"><meta name="title-ja" content="{t["ja"]}">
<meta name="description" content="{DESC}">
<meta property="og:title" content="燼燈深淵 Emberlamp Abyss">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="https://ember.sanbaofang.com/img/og.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0c0a09">
<link rel="icon" href="{up}img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{up}img/apple-touch-icon.png">
<link rel="stylesheet" href="{up}style.css">
<script src="{up}lang.js"></script>
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{up}"><img src="{up}img/icon-192.png" alt="">{L("燼燈深淵", "Emberlamp Abyss", "燼燈深淵")}</a>
<nav>{navl(0, "")}{navl(1, "support/")}{navl(2, "privacy/")}</nav>
<div class="langs"><button type="button" data-set="zh-Hant">繁中</button><button type="button" data-set="en">EN</button><button type="button" data-set="ja">日本語</button></div>
</div></header>
{body}
<footer><div class="wrap">{L("燼燈深淵", "Emberlamp Abyss", "燼燈深淵")}・指數三寶飯製作・<a href="mailto:{MAIL}">{MAIL}</a></div></footer>
</body>
</html>
'''

def shots(l):
    alts = {'1-combat': '戰鬥', '4-classes': '選職業', '6-city': '點亮燈城', '7-gallery': '畫廊'}
    return ''.join(f'<img data-l="{l}" src="img/shot-{l}-{n}.jpg" alt="{a}" loading="lazy" width="440" height="956">' for n, a in alts.items())

INDEX = f'''<div class="hero"><img src="img/hero.jpg" alt="" width="1600" height="900"><div class="in">
<h1>燼燈深淵</h1><div class="en">EMBERLAMP ABYSS</div>
{L("提一盞燈，走下十層地窟。<br>燈油燒乾，黑暗就會開始進食。", "Carry a lamp ten floors down.<br>When the oil runs dry, the dark begins to feed.", "灯をひとつ提げて、十層の地窟へ。<br>灯油が尽きれば、闇が喰らいはじめる。", "p")}
<div class="soon"><span>App Store</span><span>Google Play</span><span>Steam</span><span>{L("即將推出", "Coming soon", "近日公開")}</span></div>
</div></div>
<main class="wrap">
<section>
<h2>{L("光，就是生命", "Light is life", "光こそ命")}</h2>
{L("回合制的地城探險。每一局的地圖、怪物、寶物都不一樣；死了就重來，但你帶回來的餘燼，會讓下一趟走得更遠。", "A turn-based roguelike. Every descent is different: new maps, monsters and treasure. Death is permanent, but the embers you bring back carry you further next time.", "ターン制のローグライク。マップも怪物も宝も毎回ちがう。死ねば最初から——けれど持ち帰った残り火が、次の旅をもう少し深くしてくれる。", "p class=\"lead\"")}
<ul class="feats">
<li>{L("<b>燈油就是時間</b>遮住燈可以躲過怪物，卻也看不見腳下的陷阱。", "<b>Oil is time</b>Hood your lamp to slip past them — and walk blind into traps.", "<b>灯油は時間</b>灯を覆えば怪物の目を逃れられるが、足元の罠も見えなくなる。", "div")}</li>
<li>{L("<b>八種職業</b>劍士、提燈人、燈巫、燈僧、夜行者、符師、狂戰士、送燈人，每個人都有自己下井的理由。", "<b>Eight classes</b>From the Swordsman to the Lamp Ferrier — each has their own reason to go down the well.", "<b>八つの職業</b>剣士から送り灯まで。誰にも、井戸へ下りる理由がある。", "div")}</li>
<li>{L("<b>點亮燈城</b>帶回來的餘燼，一區一區點亮你的家。", "<b>Relight Lamp City</b>Spend the embers you bring home to light your city, district by district.", "<b>灯城に灯を</b>持ち帰った残り火で、街を一区ずつ灯していく。", "div")}</li>
<li>{L("<b>41 張插圖</b>每個職業五種畫風，從水墨到金碧山水。", "<b>41 illustrations</b>Five styles per class, from ink wash to gold-and-blue landscape.", "<b>41 枚の挿絵</b>職業ごとに五つの画風。水墨から金碧山水まで。", "div")}</li>
<li>{L("<b>漢字或像素</b>同一座深淵，兩種看法，隨時切換。", "<b>Hanzi or pixel art</b>Same abyss, two ways to see it. Switch any time.", "<b>漢字かドット絵か</b>同じ深淵を、ふたつの見え方で。", "div")}</li>
<li>{L("<b>免費試玩，一次買斷</b>沒有廣告、不用連網、不收集任何資料。", "<b>Free to try, pay once</b>No ads, no internet required, no data collected.", "<b>無料で遊べて買い切り</b>広告なし、オフライン、データ収集なし。", "div")}</li>
</ul>
</section>
<section>
<h2>{L("畫面", "Screenshots", "スクリーンショット")}</h2>
<div class="shots">{shots("zh-Hant")}{shots("en")}{shots("ja")}</div>
</section>
<section>
<h2>{L("燈城", "Lamp City", "灯城")}</h2>
{L("百年來第一次，燈城有了光。可是還有很多街巷是暗的。", "For the first time in a hundred years, Lamp City has light. But many of its streets are still dark.", "百年ぶりに、灯城に光が戻った。けれど、まだ暗い通りがたくさんある。", "p class=\"lead\"")}
<figure><img class="wide" src="img/city.jpg" alt="" loading="lazy" width="1024" height="576"></figure>
</section>
</main>'''

def faq(items):
    return ''.join(f'<div class="card">{L(*[f"<h3>{q}</h3>{a}" for q, a in it], tag="div")}</div>' for it in items)

SUPPORT_ITEMS = [
 [("怎麼購買完整版？", "<p>在選職業畫面點任一個標著「完整版」的職業，或在畫廊點「完整版」的格子，就會打開購買頁。完整版一次買斷，沒有其他付費。</p>"),
  ("How do I buy the full version?", "<p>On the class screen, tap any class marked “Full version”, or tap a “Full version” tile in the Gallery, to open the purchase page. It is a single purchase with nothing else to buy.</p>"),
  ("完全版はどうやって買える？", "<p>職業選択画面で「完全版」と表示された職業、またはギャラリーの「完全版」の枠をタップすると購入画面が開く。買い切りで、ほかの課金はない。</p>")],
 [("換手機或重新安裝後，完整版不見了", "<p>打開購買頁，按下方的「恢復購買」。請用當初購買時的 Apple ID 或 Google 帳號登入。</p>"),
  ("I reinstalled or changed phones and lost the full version", "<p>Open the purchase page and tap “Restore purchase”. Make sure you are signed in with the same Apple ID or Google account you bought it with.</p>"),
  ("機種変更・再インストールで完全版が消えた", "<p>購入画面を開き、下の「購入を復元」を押す。購入したときと同じ Apple ID または Google アカウントでサインインしておくこと。</p>")],
 [("換手機時，怎麼保留遊戲紀錄？", "<p>紀錄只存在你的裝置上。換手機前：</p><ul><li>舊手機：設定 →「紀錄備份」→「複製」，把備份碼存在備忘錄或傳給自己。</li><li>新手機：設定 →「紀錄備份」→ 貼上備份碼 → 按兩次「還原」。</li></ul><p>備份碼包含通關紀錄、畫廊、燈城、餘燼與工坊，不含正在進行的那一局。</p>"),
  ("How do I keep my records when changing phones?", "<p>Your records live only on your device. Before switching:</p><ul><li>Old phone: Settings → “Back up records” → “Copy”, and keep the code in your notes or send it to yourself.</li><li>New phone: Settings → “Back up records” → paste the code → tap “Restore” twice.</li></ul><p>The code includes clears, gallery, Lamp City, embers and the Workshop, but not a run in progress.</p>"),
  ("機種変更のとき、記録を引き継ぐには？", "<p>記録は端末の中にだけ保存されている。機種変更の前に：</p><ul><li>古い端末：設定 →「記録のバックアップ」→「コピー」。コードをメモに保存するか、自分に送っておく。</li><li>新しい端末：設定 →「記録のバックアップ」→ コードを貼り付け →「復元」を二回押す。</li></ul><p>踏破、ギャラリー、灯城、残り火、工房が含まれる。進行中の冒険は含まれない。</p>")],
 [("怎麼操作？", "<ul><li>移動：手機用畫面上的方向鍵或搖桿（可在設定切換），電腦用方向鍵、WASD 或數字鍵。點地圖可以自動走過去。</li><li>攻擊：直接走向敵人。</li><li>遮燈：躲過怪物的眼睛，但視野會變小。</li><li>「探索」自動走向還沒去過的地方；「搜索」撿東西、開寶箱、下樓。</li></ul><p>遊戲裡的「說明」有完整的按鍵表與圖例。</p>"),
  ("How do I play?", "<ul><li>Move: on phones, the on-screen pad or stick (switch in Settings); on computers, arrow keys, WASD or the number pad. Tap the map to walk there.</li><li>Attack: walk into an enemy.</li><li>Hood: hide from monsters, at the cost of your sight.</li><li>“Explore” walks toward unexplored areas; “Search” picks things up, opens chests and takes the stairs.</li></ul><p>In-game “Help” has the full key list and legend.</p>"),
  ("操作方法は？", "<ul><li>移動：スマホは画面の方向キーかスティック（設定で切り替え）、パソコンは矢印キー、WASD、テンキー。マップをタップするとそこまで歩く。</li><li>攻撃：敵に向かって歩く。</li><li>遮灯：怪物の目を逃れるが、視界が狭くなる。</li><li>「探索」は未踏の場所へ自動で進み、「捜索」で拾う・宝箱を開ける・階段を下りる。</li></ul><p>ゲーム内の「説明」にキー一覧と凡例がある。</p>")],
 [("需要連網嗎？", "<p>不需要。遊戲完全離線，不需要帳號，也不收集任何資料（見<a href=\"../privacy/\">隱私權政策</a>）。</p>"),
  ("Do I need an internet connection?", "<p>No. The game is fully offline, needs no account and collects no data (see the <a href=\"../privacy/\">privacy policy</a>).</p>"),
  ("通信は必要？", "<p>不要。完全にオフラインで、アカウントも不要、データも収集しない（<a href=\"../privacy/\">プライバシーポリシー</a>を参照）。</p>")],
 [("回報問題或給建議", f"<p>歡迎寫信到 <a href=\"mailto:{MAIL}\">{MAIL}</a>。回報問題時，請附上手機型號、系統版本，以及遊戲「關於」頁上的版本號；有截圖更好。</p>"),
  ("Report a problem or send feedback", f"<p>Write to <a href=\"mailto:{MAIL}\">{MAIL}</a>. For problems, please include your device model, OS version and the game version shown on the About page; a screenshot helps.</p>"),
  ("不具合の報告・ご意見", f"<p><a href=\"mailto:{MAIL}\">{MAIL}</a> までどうぞ。不具合の場合は、端末の機種、OS のバージョン、ゲームの「このゲームについて」画面のバージョンを添えてほしい。スクリーンショットがあると助かる。</p>")],
]
SUPPORT = f'''<main class="wrap doc">
<h1>{L("技術支援", "Support", "サポート")}</h1>
{L("常見問題。找不到答案的話，歡迎來信。", "Frequently asked questions. If you can't find your answer, just write to us.", "よくある質問。答えが見つからなければ、メールでどうぞ。", "p class=\"sub\"")}
{faq(SUPPORT_ITEMS)}
</main>'''

def privacy_body():
    src = open(os.path.join(D, 'privacy-src.html'), encoding='utf-8').read()
    return src

os.makedirs(os.path.join(D, 'support'), exist_ok=True); os.makedirs(os.path.join(D, 'privacy'), exist_ok=True)
open(os.path.join(D, 'index.html'), 'w', encoding='utf-8').write(page('index', INDEX, ''))
open(os.path.join(D, 'support', 'index.html'), 'w', encoding='utf-8').write(page('support', SUPPORT, '../'))
open(os.path.join(D, 'privacy', 'index.html'), 'w', encoding='utf-8').write(page('privacy', privacy_body(), '../'))
print('ok')
