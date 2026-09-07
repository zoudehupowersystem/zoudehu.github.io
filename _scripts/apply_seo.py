from pathlib import Path
import json
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
s = re.sub(
    r'<title>.*?</title>',
    '<title>邹德虎（Dehu Zou）｜电力系统仿真、调度自动化与工业软件研发</title>',
    s,
    count=1,
    flags=re.S,
)
s = re.sub(
    r'<meta name="description"\s*\n?\s*content=".*?"\s*/>',
    '<meta name="description" content="邹德虎（Dehu Zou），高级工程师、电力系统研发架构师。长期从事电力系统建模仿真、实时电磁暂态仿真（EMT）、电网调度自动化与工业软件研发，ADS-RTSim 实时仿真平台负责人，OPSEN 开源项目发起人。" />',
    s,
    count=1,
    flags=re.S,
)

profile_schema = '''
  <link rel="canonical" href="https://zoudehupowersystem.github.io/zoudehu.github.io/" />
  <meta property="og:type" content="profile" />
  <meta property="og:title" content="邹德虎（Dehu Zou）｜电力系统仿真、调度自动化与工业软件研发" />
  <meta property="og:description" content="邹德虎（Dehu Zou），高级工程师、电力系统研发架构师。长期从事电力系统建模仿真、实时电磁暂态仿真（EMT）、电网调度自动化与工业软件研发。" />
  <meta property="og:url" content="https://zoudehupowersystem.github.io/zoudehu.github.io/" />
  <meta property="og:image" content="https://zoudehupowersystem.github.io/zoudehu.github.io/zoudehu.jpg" />
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ProfilePage",
    "@id": "https://zoudehupowersystem.github.io/zoudehu.github.io/#profile",
    "url": "https://zoudehupowersystem.github.io/zoudehu.github.io/",
    "name": "邹德虎（Dehu Zou）个人主页",
    "description": "邹德虎（Dehu Zou），高级工程师、电力系统研发架构师。长期从事电力系统建模仿真、实时电磁暂态仿真（EMT）、电网调度自动化与工业软件研发。",
    "dateModified": "2026-09-07",
    "mainEntity": {
      "@type": "Person",
      "@id": "https://zoudehupowersystem.github.io/zoudehu.github.io/#dehu-zou",
      "name": "邹德虎",
      "alternateName": "Dehu Zou",
      "url": "https://zoudehupowersystem.github.io/zoudehu.github.io/",
      "image": "https://zoudehupowersystem.github.io/zoudehu.github.io/zoudehu.jpg",
      "jobTitle": "电力系统研发架构师、技术总监 / Power System R&D Architect and Technical Director",
      "description": "高级工程师，长期从事电力系统建模仿真、实时电磁暂态仿真、电网调度自动化与工业软件研发。",
      "knowsAbout": [
        "Power systems",
        "Electromagnetic transient simulation",
        "Real-time EMT simulation",
        "Power system modelling and simulation",
        "Grid dispatch and automation",
        "Industrial software engineering",
        "High-performance C++"
      ],
      "sameAs": ["https://github.com/zoudehupowersystem"]
    }
  }
  </script>
'''
if '#dehu-zou' not in s:
    s = s.replace(
        '  <meta name="theme-color" content="#0B1F3A" />',
        '  <meta name="theme-color" content="#0B1F3A" />\n' + profile_schema,
    )
p.write_text(s, encoding='utf-8')

p = Path('_layouts/article.html')
s = p.read_text(encoding='utf-8')
old = '''  <title>{{ page.title }}｜邹德虎的博客</title>
  <meta name="description" content="邹德虎的博客：电力系统、工程技术、计算与仿真。" />'''
new = '''  {% capture default_seo_title %}{{ page.title }}｜邹德虎 Dehu Zou{% endcapture %}
  {% assign seo_title = page.seo_title | default: default_seo_title | strip %}
  {% capture fallback_description %}{{ content | strip_html | strip_newlines | replace: '  ', ' ' | truncate: 180 }}{% endcapture %}
  {% assign seo_description = page.description | default: fallback_description | strip %}
  <title>{{ seo_title | escape }}</title>
  <meta name="description" content="{{ seo_description | escape }}" />
  <meta name="author" content="邹德虎 / Dehu Zou" />
  <link rel="canonical" href="https://zoudehupowersystem.github.io/zoudehu.github.io{{ page.url }}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{{ seo_title | escape }}" />
  <meta property="og:description" content="{{ seo_description | escape }}" />
  <meta property="og:url" content="https://zoudehupowersystem.github.io/zoudehu.github.io{{ page.url }}" />
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": {{ page.title | jsonify }},
    "description": {{ seo_description | jsonify }},
    "url": {{ 'https://zoudehupowersystem.github.io/zoudehu.github.io' | append: page.url | jsonify }},
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": {{ 'https://zoudehupowersystem.github.io/zoudehu.github.io' | append: page.url | jsonify }}
    },
    "author": {
      "@type": "Person",
      "@id": "https://zoudehupowersystem.github.io/zoudehu.github.io/#dehu-zou",
      "name": "邹德虎",
      "alternateName": "Dehu Zou",
      "url": "https://zoudehupowersystem.github.io/zoudehu.github.io/",
      "sameAs": ["https://github.com/zoudehupowersystem"]
    },
    "publisher": {
      "@type": "Person",
      "@id": "https://zoudehupowersystem.github.io/zoudehu.github.io/#dehu-zou",
      "name": "邹德虎 / Dehu Zou"
    },
    "inLanguage": "zh-CN"
  }
  </script>'''
if old not in s:
    raise RuntimeError('Expected article head block not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')

def clean_text(x: str) -> str:
    x = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', x)
    x = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', x)
    x = re.sub(r'<[^>]+>', '', x)
    x = re.sub(r'[`*_>#|]', '', x)
    x = re.sub(r'\$[^$]+\$', '', x)
    x = re.sub(r'https?://\S+', '', x)
    x = re.sub(r'\s+', ' ', x).strip()
    return x

def first_description(body: str, title: str) -> str:
    for chunk in re.split(r'\n\s*\n', body):
        t = clean_text(chunk)
        if not t:
            continue
        if t.startswith(title):
            continue
        if t.startswith('作者：') or t.startswith('202'):
            continue
        if chunk.lstrip().startswith(('#', '$$', '```', '|', '![', '<style', '<div')):
            continue
        if re.match(r'^\d+[\.,、]\s', t):
            continue
        if len(t) >= 45:
            return (t[:165] + '…') if len(t) > 165 else t
    return f'{title}。邹德虎（Dehu Zou）的电力系统、工程技术与计算仿真专题文章。'

custom_titles = {
    '深入理解潮流计算': '深入理解潮流计算：工程视角、节点类型与牛顿法｜邹德虎 Dehu Zou',
    '矩阵思维下的潮流计算': '矩阵思维下的潮流计算：Ybus、复功率雅可比与高性能实现｜邹德虎 Dehu Zou',
    '论电力系统仿真': '论电力系统仿真：EMT、实时仿真与工业软件｜邹德虎 Dehu Zou',
    '谈谈电力系统状态估计': '电力系统状态估计：工程实践、量测与数据处理｜邹德虎 Dehu Zou',
    'C++优化技术': 'C++优化技术：缓存、并行与高性能工程实践｜邹德虎 Dehu Zou',
    '计算机系统之旅': '计算机系统之旅：处理器、存储器与系统级编程｜邹德虎 Dehu Zou',
    '职业生涯回顾与思考': '邹德虎（Dehu Zou）的职业生涯回顾与工程研发思考',
}

for p in sorted(Path('.').glob('*.md')):
    if p.name in {'README.md', '曼尼托巴水电局的创业史.md', 'manitoba-hydro-pscad-rtds-history.md'}:
        continue
    text = p.read_text(encoding='utf-8')
    m = re.match(r'\A---\s*\n(.*?)\n---\s*\n(.*)\Z', text, flags=re.S)
    if not m or 'layout: article' not in m.group(1):
        continue
    fm, body = m.group(1), m.group(2)
    tm = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, flags=re.M)
    if not tm:
        continue
    title = tm.group(1).strip().strip('"\'')
    seo_title = custom_titles.get(title, f'{title}｜邹德虎 Dehu Zou')
    desc = first_description(body, title)
    fm_lines = [
        line for line in fm.splitlines()
        if not line.startswith('seo_title:') and not line.startswith('description:')
    ]
    fm_lines.append('seo_title: ' + json.dumps(seo_title, ensure_ascii=False))
    fm_lines.append('description: ' + json.dumps(desc, ensure_ascii=False))
    p.write_text('---\n' + '\n'.join(fm_lines) + '\n---\n\n' + body.lstrip('\n'), encoding='utf-8')

zh = Path('曼尼托巴水电局的创业史.md')
text = zh.read_text(encoding='utf-8')
m = re.match(r'\A---\s*\n(.*?)\n---\s*\n(.*)\Z', text, flags=re.S)
if not m:
    raise RuntimeError('Chinese Manitoba front matter not found')
body = m.group(2)
fm = '''layout: manitoba
title: "曼尼托巴水电局的创业史"
lang: zh-CN
seo_title: "曼尼托巴水电局的创业史：PSCAD、RTDS 与实时电磁仿真的诞生｜邹德虎"
description: "从纳尔逊河HVDC工程出发，梳理Manitoba Hydro、Dennis Woodford、EMTDC/PSCAD、Manitoba HVDC Research Centre、RTDS Technologies及曼尼托巴大学之间数十年的技术研发、工程验证与产业化历史。"'''
zh.write_text('---\n' + fm + '\n---\n\n' + body.lstrip('\n'), encoding='utf-8')

en = Path('manitoba-hydro-pscad-rtds-history.md')
text = en.read_text(encoding='utf-8')
m = re.match(r'\A---\s*\n(.*?)\n---\s*\n(.*)\Z', text, flags=re.S)
if not m:
    raise RuntimeError('English Manitoba front matter not found')
body = m.group(2)
fm = '''layout: manitoba
title: "From the Nelson River to PSCAD and RTDS: Manitoba’s Power-System Simulation Story"
lang: en
seo_title: "History of PSCAD and RTDS: Manitoba Hydro, EMTDC and Real-Time Simulation | Dehu Zou"
description: "A technical history of Manitoba Hydro, Dennis Woodford, EMTDC/PSCAD, the Manitoba HVDC Research Centre, RTDS Technologies, the University of Manitoba, real-time EMT simulation, and the commercialization path from utility engineering problems to global simulation products."'''
en.write_text('---\n' + fm + '\n---\n\n' + body.lstrip('\n'), encoding='utf-8')
