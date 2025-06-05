import random

# 日本人の名前リスト（例）
japanese_names = [
    "佐藤 大輔", "鈴木 一郎", "高橋 健太", "田中 翔太", "伊藤 直樹",
    "渡辺 拓海", "山本 悠斗", "中村 亮", "小林 海斗", "加藤 陸",
    "吉田 颯太", "山田 智也", "佐々木 大地", "山口 直人", "松本 悠真",
    "井上 大和", "木村 陽斗", "林 悠人", "斎藤 陽太", "清水 大輝",
    "山崎 颯真", "森 拓真", "池田 陸斗", "橋本 悠生", "阿部 颯汰",
    "石川 陽翔", "山下 大悟", "中島 陽大", "小川 陽斗", "前田 悠斗",
    "藤田 大翔", "岡田 陽斗", "後藤 颯太", "村上 悠真", "遠藤 大地",
    "青木 陽太", "坂本 颯真", "福田 陸斗", "太田 悠斗", "三浦 大輝",
    "西村 颯汰"
]

# 外国人の名前リスト（例）
foreign_names = [
    "John Smith", "Michael Johnson", "David Brown", "James Williams", "Robert Jones",
    "William Garcia", "Daniel Miller", "Matthew Davis", "Anthony Wilson", "Mark Taylor"
]

athletes = []

# 日本人40人
for name in japanese_names:
    age = random.randint(20, 30)
    time = round(random.uniform(9.56, 12.99), 2)
    athletes.append({
        "name": name,
        "age": age,
        "time": time,
        "nationality": "日本"
    })

# 外国人10人
for name in foreign_names:
    age = random.randint(20, 30)
    time = round(random.uniform(9.56, 12.99), 2)
    athletes.append({
        "name": name,
        "age": age,
        "time": time,
        "nationality": "外国"
    })

# タイムが速い順にソート
data_sorted = sorted(athletes, key=lambda x: x["time"])

# 結果表示
print(f"{'順位':<4} {'名前':<15} {'年齢':<4} {'国籍':<4} {'タイム':<5}")
for i, athlete in enumerate(data_sorted, 1):
    print(f"{i:<4} {athlete['name']:<15} {athlete['age']:<4} {athlete['nationality']:<4} {athlete['time']:<5}")

    