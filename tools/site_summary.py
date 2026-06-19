import json
import os
from typing import Dict, List

# 示例站点资料（不进行网络请求，仅用于演示结构化输出）
SITE_DATA = {
    "name": "CCTV娱乐站点",
    "url": "https://cctv-c7entertainment.com",
    "tags": ["c7娱乐", "综艺", "在线视频", "明星"],
    "description": "提供最新娱乐资讯、综艺节目回放与明星动态的综合平台。",
    "keywords": ["c7娱乐", "娱乐新闻", "综艺节目"],
    "category": "娱乐门户",
}

SITE_TEMPLATE = """
========================================
              站点摘要报告
========================================
站点名称:    {name}
URL:         {url}
类别:        {category}
标签:        {tag_str}
关键词:      {keyword_str}
简介:        {description}
----------------------------------------
"""

def format_list(items: List[str]) -> str:
    """将列表格式化为带逗号的字符串"""
    if not items:
        return "无"
    return ", ".join(item.strip() for item in items)

def generate_summary(data: Dict) -> str:
    """根据提供的站点资料数据生成摘要字符串"""
    tag_str = format_list(data.get("tags", []))
    keyword_str = format_list(data.get("keywords", []))
    summary = SITE_TEMPLATE.format(
        name=data.get("name", "未知站点"),
        url=data.get("url", ""),
        category=data.get("category", "未分类"),
        tag_str=tag_str,
        keyword_str=keyword_str,
        description=data.get("description", "暂无描述"),
    )
    return summary.strip()

def load_site_data(filepath: str = "") -> Dict:
    """尝试从文件加载站点资料，若文件不存在则返回默认内置数据"""
    if filepath and os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("警告：无法解析站点数据文件，使用内置默认数据。")
    # 返回内置默认数据
    return dict(SITE_DATA)

def save_summary_to_file(summary: str, output_path: str = "site_summary.txt") -> None:
    """将摘要内容写入文本文件"""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"摘要已写入 {output_path}")
    except IOError as e:
        print(f"写入文件时出错: {e}")

def main() -> None:
    """主函数：读取站点资料，生成摘要并输出"""
    # 可选的 JSON 配置文件路径（如果存在则读取）
    config_path = "site_data.json"
    data = load_site_data(config_path)

    # 生成摘要
    summary = generate_summary(data)

    # 输出到控制台
    print(summary)

    # 保存到文件
    save_summary_to_file(summary)

if __name__ == "__main__":
    main()