from flask import Flask, render_template

app = Flask(__name__)

# 产品数据
products = [
    {
        'id': 1,
        'name': '优质咖啡',
        'description': '来自哥伦比亚的高山咖啡豆，香气浓郁，口感醇厚。',
        'image': 'coffee.jpg',
        'price': '¥98'
    },
    {
        'id': 2,
        'name': '手工茶具',
        'description': '传统工艺制作的陶瓷茶具，每一件都是独一无二的艺术品。',
        'image': 'teaset.jpg',
        'price': '¥258'
    },
    {
        'id': 3,
        'name': '有机蜂蜜',
        'description': '纯天然无添加的有机蜂蜜，来自深山的花海。',
        'image': 'honey.jpg',
        'price': '¥68'
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)