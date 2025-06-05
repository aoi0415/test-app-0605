import random

# 食べ物の商品名リスト（例：50個）
product_names = [
    "りんご", "バナナ", "みかん", "ぶどう", "いちご", "メロン", "スイカ", "パイナップル", "キウイ", "もも",
    "レタス", "キャベツ", "トマト", "きゅうり", "にんじん", "じゃがいも", "たまねぎ", "ピーマン", "なす", "ほうれん草",
    "牛乳", "ヨーグルト", "チーズ", "卵", "バター", "食パン", "クロワッサン", "ロールパン", "ベーグル", "フランスパン",
    "ハム", "ソーセージ", "ベーコン", "鶏肉", "豚肉", "牛肉", "鮭", "サバ", "アジ", "イカ",
    "おにぎり", "お弁当", "サンドイッチ", "お寿司", "カレー", "ラーメン", "うどん", "そば", "パスタ", "ピザ"
]

# 商品ごとの価格（100円～5000円でランダムに設定）
product_prices = {name: random.randint(100, 5000) for name in product_names}

# かごの中身をランダムに選択（例：5～15個の商品を選ぶ）
def get_basket():
    basket_size = random.randint(5, 15)
    return random.sample(product_names, basket_size)

# カメラでかごの中身を"認識"（ここではランダムに選択）
basket = get_basket()

# 合計金額を計算
total = sum(product_prices[item] for item in basket)

# 結果表示
print("かごの中身:")
for item in basket:
    print(f"{item}: {product_prices[item]}円")
print(f"\n合計金額: {total}円")
