import csv
import os

# --- 配置区域 ---
csv_file = 'words.csv'
output_folder = '俄语单词库'
# ----------------

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def create_md_files():
    try:
        with open(csv_file, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                # 即使 CSV 里有例句列，我们现在只读取这两列
                word = row['单词'].strip()
                translation = row['中文翻译'].strip()

                # 最简洁的闪卡模板
                md_content = f"""---
tags: flashcards/俄语
---

# {word}

{word} :: {translation}

---
[[俄语学习主页]]
"""

                file_path = os.path.join(output_folder, f"{word}.md")
                with open(file_path, mode='w', encoding='utf-8') as md_file:
                    md_file.write(md_content)
                count += 1

            print(f"✅ 完成！已重新生成 {count} 个纯单词文件。")

    except KeyError as e:
        print(f"❌ 报错：找不到列名 {e}。请确认 CSV 第一行包含 '单词' 和 '中文翻译'。")
    except Exception as e:
        print(f"❌ 发生错误: {e}")


if __name__ == "__main__":
    create_md_files()