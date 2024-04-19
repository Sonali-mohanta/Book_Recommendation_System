# from flask import Flask, render_template,request
# import pickle
# import numpy as np
# popular_df = pickle.load(open('popular.pkl', 'rb'))
# pt = pickle.load(open('pt.pkl','rb'))
# books = pickle.load(open('books.pkl','rb'))
# similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

# app = Flask(__name__)

# @app.route('/home')
# def index():
#     return render_template('home.html',
#                            book_name = list(popular_df['Book-Title'].values),
#                            author = list(popular_df['Book-Author'].values),
#                            image = list(popular_df['Image-URL-M'].values),
#                            votes = list(popular_df['num_ratings'].values),
#                            rating = list(popular_df['avg_rating'].values)
#                            )
# @app.route('/recommend')
# def recommend_ui():
#     return render_template('recommend.html')

# @app.route('/recommend_books',methods=['post'])
# def recommend():
#     user_input = request.form.get('user_input')
#     index = np.where(pt.index == user_input)[0][0]
#     similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

# @app.route('/register')
# def register():
#     return render_template('register.html')


# @app.route('/')
# def login():
#     return render_template('index.html')



#     data = []
#     for i in similar_items:
#         item = []
#         temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#         item.extend(temp_df.drop_duplicates('Book-Title')['Book-Title'])
#         item.extend(temp_df.drop_duplicates('Book-Title')['Book-Author'])
#         item.extend(temp_df.drop_duplicates('Book-Title')['Image-URL-M'])

#         data.append(item)

#     print(data)

#     return render_template('recommend.html',data=data)

# if __name__ == '__main__':
#     app.run(debug=True)








from flask import Flask, render_template,request, redirect, url_for
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('home.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes = list(popular_df['num_ratings'].values),
                           rating = list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Title'])
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Author'])
        item.extend(temp_df.drop_duplicates('Book-Title')['Image-URL-M'])
        data.append(item)

    return render_template('recommend.html', data=data)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/logout')
def logout():
    # Add logout functionality
    return redirect(url_for('login'))  # Redirect to the login page after logout

if __name__ == '__main__':
    app.run(debug=True)
