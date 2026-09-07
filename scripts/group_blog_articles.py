from pathlib import Path
import re

p = Path("index.html")
s = p.read_text(encoding="utf-8")

css = r'''
    /* Blog topic groups */
    .article-groups {
      display: grid;
      gap: 18px;
    }
    .article-group {
      padding: 16px;
      border: 1px solid rgba(255,255,255,.10);
      border-radius: 15px;
      background: linear-gradient(180deg, rgba(255,255,255,.035), rgba(255,255,255,.018));
    }
    .article-group-head {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 14px;
      margin-bottom: 12px;
      padding-bottom: 11px;
      border-bottom: 1px solid rgba(255,255,255,.07);
    }
    .article-group-title {
      margin: 0;
      color: rgba(255,255,255,.92);
      font-size: 16px;
      line-height: 1.45;
      font-weight: 700;
      letter-spacing: .15px;
    }
    .article-group-desc {
      margin-top: 4px;
      color: var(--faint);
      font-size: 12.5px;
      line-height: 1.55;
    }
    .article-group-count {
      flex: 0 0 auto;
      padding: 4px 8px;
      border-radius: 999px;
      border: 1px solid rgba(91,181,255,.16);
      background: rgba(91,181,255,.055);
      color: rgba(155,231,255,.55);
      font-family: var(--mono);
      font-size: 11px;
    }
    .article-group .articles-grid {
      gap: 8px 12px;
    }
    .article-group .article-item {
      min-height: 44px;
      background: rgba(255,255,255,.025);
    }
    .article-group .article-item span {
      font-size: 13.5px;
    }
    .article-group .article-item small {
      color: rgba(155,231,255,.58);
    }
    @media (max-width: 700px) {
      .article-group { padding: 13px; }
      .article-group-head { gap: 10px; }
      .article-group-title { font-size: 15px; }
    }
'''

if '/* Blog topic groups */' not in s:
    s = s.replace('    /* Responsive */', css + '\n    /* Responsive */', 1)


def item(href, title, tag=None):
    meta = f'<small>{tag}</small>' if tag else ''
    return (
        f'              <a class="article-item" role="listitem" href="{href}">\n'
        f'                <span>{title}</span>{meta}\n'
        f'              </a>'
    )


groups = [
    (
        '电力系统原理与计算',
        '从物理机理、潮流、短路和对称分量，到状态估计、频率与控制。',
        [
            ('从物理学出发理解电力系统.html', '从物理学出发理解电力系统', None),
            ('深入理解潮流计算.html', '深入理解潮流计算', None),
            ('矩阵思维下的潮流计算.html', '矩阵思维下的潮流计算', 'NEW'),
            ('重温牛顿-拉夫逊法.html', '重温牛顿-拉夫逊法', None),
            ('深入理解对称分量法.html', '深入理解对称分量法', None),
            ('电力系统近似常数与近似公式.html', '电力系统近似常数与近似公式', None),
            ('短路与短路比.html', '短路与短路比', None),
            ('谈谈电力系统状态估计.html', '谈谈电力系统状态估计', None),
            ('从音乐到电力系统一次调频.html', '从音乐到电力系统一次调频', None),
            ('电力系统控制的思考.html', '电力系统控制的思考', None),
        ],
    ),
    (
        '仿真、调度与工程实践',
        '实时仿真、调度自动化、二次设备、工业软件，以及工程研发与产业化实践。',
        [
            ('职业生涯回顾与思考.html', '职业生涯回顾与思考', None),
            ('曼尼托巴水电局的创业史.html', '曼尼托巴系列：曼尼托巴水电局的创业史', '中文'),
            ('manitoba-hydro-pscad-rtds-history.html', 'Manitoba Series: From the Nelson River to PSCAD and RTDS', 'EN'),
            ('电网调度技术思考.html', '电网调度技术思考', None),
            ('论电力系统仿真.html', '论电力系统仿真', None),
            ('电力系统仿真会议参会记录.html', '电力系统仿真会议参会记录', None),
            ('谈谈电力系统嵌入式装置.html', '谈谈电力系统嵌入式装置', None),
            ('电力系统二次设备科普.html', '电力系统二次设备科普', None),
            ('论电力安全生产.html', '论电力安全生产', None),
            ('论电力数字化转型.html', '论电力数字化转型', None),
            ('工业系统演化与设计.html', '工业系统演化与设计', None),
            ('论系统工程.html', '论系统工程', None),
        ],
    ),
    (
        '计算机与信息技术',
        '高性能计算、系统软件、编程语言、通信，以及计算机体系结构。',
        [
            ('电力系统中的编程语言.html', '电力系统中的编程语言', None),
            ('电力通信科普.html', '电力通信科普', None),
            ('分布式计算机系统.html', '分布式计算机系统', None),
            ('计算机中的基础数学函数.html', '计算机中的基础数学函数', None),
            ('C++优化技术.html', 'C++优化技术', None),
            ('计算机系统之旅.html', '计算机系统之旅', None),
            ('谈谈汇编语言.html', '谈谈汇编语言', None),
        ],
    ),
]

blocks = []
for title, desc, entries in groups:
    items = '\n'.join(item(*x) for x in entries)
    block = (
        f'          <section class="article-group" aria-label="{title}">\n'
        f'            <div class="article-group-head">\n'
        f'              <div>\n'
        f'                <h3 class="article-group-title">{title}</h3>\n'
        f'                <div class="article-group-desc">{desc}</div>\n'
        f'              </div>\n'
        f'              <div class="article-group-count">{len(entries)} 篇</div>\n'
        f'            </div>\n'
        f'            <div class="articles-grid" role="list">\n'
        f'{items}\n'
        f'            </div>\n'
        f'          </section>'
    )
    blocks.append(block)

replacement = (
    '        <!-- ARTICLES -->\n'
    '        <div class="section" id="articles">\n'
    '          <h2>博客文章</h2>\n'
    '          <div class="section-note">按主题浏览，共 29 篇。</div>\n'
    '          <div class="article-groups">\n'
    + '\n'.join(blocks)
    + '\n          </div>\n'
    '        </div>\n\n'
    '        <!-- EDUCATION -->'
)

pattern = re.compile(r'        <!-- ARTICLES -->.*?        <!-- EDUCATION -->', re.S)
if not pattern.search(s):
    raise RuntimeError('Article section markers not found')

s = pattern.sub(replacement, s, count=1)
p.write_text(s, encoding='utf-8')
