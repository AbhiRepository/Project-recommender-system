from flask import Flask, render_template, url_for, flash, redirect, request, session, logging, jsonify
from forms import RegistrationForm, LoginForm, RatingForm
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from functools import wraps
from flask_wtf import CSRFProtect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation, cosine
from sklearn.metrics import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys, os

global k,metric
k=2
metric='cosine'
temp_user_id = 12

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Abhishek@123'
app.config['MYSQL_DB'] = 'finalproject'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# -------------- ### this is route for liking the article using ### ---------- # 

@app.route("/articleone")
def articleone():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 1, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked article 1", 'success')
    return redirect(url_for('battery'))

@app.route("/articletwo")
def articletwo():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 2, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 2", 'success')
    return redirect(url_for('battery'))

@app.route("/articlethree")
def articlethree():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 3, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 3", 'success')
    return redirect(url_for('battery'))

@app.route("/articlefour")
def articlefour():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 4, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 4", 'success')
    return redirect(url_for('battery'))

@app.route("/articlefive")
def articlefive():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 5, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 5", 'success')
    return redirect(url_for('battery'))

@app.route("/articlesix")
def articlesix():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 6, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 6", 'success')
    return redirect(url_for('battery'))

@app.route("/articleseven")
def articleseven():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 7, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 7", 'success')
    return redirect(url_for('battery'))

@app.route("/articleeight")
def articleeight():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 8, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 

    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 8", 'success')
    return redirect(url_for('battery'))

@app.route("/articlenine")
def articlenine():
    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO user_article values(%s, %s, %s)', (user_id, 9, 1))
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        updated_rating = rating_data['rating']+1;
        cur.execute('UPDATE user_rating SET rating = %s WHERE user_id = %s', (updated_rating, session['user_id']))
        mysql.connection.commit()
    else:
        cur.execute('INSERT INTO user_rating VALUES(%s, %s)', (session['user_id'], 1))
        mysql.connection.commit() 


    # app.logger.info('dsdssdsddsdsdsdsdsd')
    flash("you have liked this article 9", 'success')
    return redirect(url_for('battery'))

# -------------- ### route for liking the article usingbutton ends here ### ---------- # 

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/feedback")
def feedback():
    return render_template('feedback.html')

@app.route("/rating")
def rating():
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM user_rating WHERE user_id = %s', [session['user_id']])
    if result:
        rating_data = cur.fetchone()
        rating = rating_data['rating']
        print rating
        return render_template('rating.html', rating=rating, username=session['username'])
    return render_template('rating.html', rating=0, username=session['username'])

@app.route("/buy")
def buy():
    user_id = session['user_id']
    product_id = 1
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user_product VALUES(%s, %s)", (user_id, product_id))
    mysql.connection.commit()
    cur.close()
    flash('You have bought Laptop', 'success')
    return redirect(url_for('shop'))


@app.route("/battery")
def battery():
    return render_template('battery.html')

@app.route("/audio")
def audio():
    return render_template('audio.html')

# Article mai change the value 3 to session['user_id']
@app.route("/article")
def article():

    articles = []


    user_id = session['user_id']
    # print "user_id", user_id

    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM user_product WHERE user_id = %s", [user_id])
    # print "no of user_product", result
    if result == 0:
        # data = cur.execute("SELECT * FROM articles")
        # datas = cur.fetchall()
        cur.close()
        datas = []
        nodata=True
        if nodata:
            print "no data is true"
        else:
            print "no data is false"
        return render_template('article.html', articles=datas, nodata=nodata)
    cur.close()

    cur = mysql.connection.cursor()
    result = cur.execute('''
        SELECT t.*
        FROM user_product t
        WHERE user_id IN(SELECT p2.user_id FROM user_product p1 INNER JOIN user_product p2
                         ON p1.product_id = p2.product_id WHERE p1.user_id = %s);
        ''', [user_id])
    if result:
        datas = cur.fetchall()
        cur.close()

        same_profile_user_id = []
        for data in datas:
            same_profile_user_id.append(data['user_id'])

        same_profile_user_id = Remove(same_profile_user_id)
        # for same_user in same_profile_user_id:
        #     print same_user

        users = []
        articles = []
        ratings = []
        # print "user_ddsdsaid", user_id
        for user_ids in same_profile_user_id:
            cur = mysql.connection.cursor()
            user_article = cur.execute("SELECT * FROM user_article WHERE user_id = %s", [user_ids])
            datas = cur.fetchall()
            cur.close()
            # for data in datas:
            #     print data 

            for data in datas:
                users.append(data['user_id'])
                articles.append(data['article_id'])
                ratings.append(data['rating'])

        print users
        print articles


        flag = True
        for user in users:
            # temp_id = session['']
            if user == session['user_id']:
                flag = False

        if flag:
            print 'new cheez chali'
            return render_template('article.html', nodata=True)

        # print users
        # print articles
        max_row = max(users)
        max_col = max(articles)
        # print "user_id", user_id
        M = np.zeros((max_row, max_col))

        for i in range(len(users)):
            M[users[i]-1][articles[i]-1] = ratings[i]

        M=pd.DataFrame(M)
        # print M

        # print "user_id", user_id
        cosine_sim = 1-pairwise_distances(M, metric="cosine")
        df = pd.DataFrame(cosine_sim)
        # print df
        
        print "user_id", user_id
        print "user idd -djfhdsjhfshkfhs", session['user_id']
        similarities, indices = findksimilarusers(user_id, df , metric='cosine')
        # print similarities, indices

        similarities = similarities.tolist()
        indices = indices[0].tolist()

        print similarities, indices

        for i in range(len(similarities)):
            print similarities[i]
            if similarities[i] == 1 or similarities[i]<0.6:
                indices[i]=-1

        indices = remove_values_from_list(indices, -1)

        print indices

        if len(indices) == 0:
            nodata = True
            return render_template('article.html', articles=datas, nodata=nodata)

        new_indices = indices

        article_id = []
        for index in new_indices:
            # print index
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT article_id FROM user_article WHERE user_id = %s", [index+1])
            if result:
                # flag = True
                article_datas = cur.fetchall()
                for article_data in article_datas:
                    article_id.append(article_data['article_id'])
            cur.close()
        
        print article_id

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM articles WHERE article_id IN %s", [article_id])
        articles = cur.fetchall()
        # print articles
        cur.close()

    # articles = []
    return render_template('article.html', articles=articles, nodata=False)

    # articles = []
    # return render_template('article.html', articles=articles, nodata=False)

@app.route("/service", methods=['GET', 'POST'])
def service():
    return render_template('service.html')

@app.route("/identify", methods=['GET', 'POST'])
def identify():
    form = RatingForm()
    if form.validate_on_submit():
        rating = form.rating.data 
        print session['user_id'], 1, rating
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_article VALUES(%s, %s, %s)", (session['user_id'], 1, rating))
        mysql.connection.commit()
        cur.close()
        flash('Rating is submitted for this article', 'success')
        return redirect(url_for('identify'))

    return render_template('identify.html', form=form)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password == confirm_password:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(user_id, username, email, password) values(%s, %s, %s, %s)", (temp_user_id, username, email, password))
            mysql.connection.commit()
            cur.close()
            flash('Account created', 'success')
            return redirect(url_for('home'))
        else:
            flash('Password do not match', 'danger')
            return redirect(url_for('login'))
        # print username, email, password, confirm_password
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == 'admin@gmail.com' and password=='admin':
            session['Logged_in'] = True
            session['username'] = email
            return redirect(url_for('home'))


        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE email = %s", [email])
        if result:
            current_user = cur.fetchone()
            db_password = current_user['password']
            if db_password == password:
                session['Logged_in'] = True
                session['username'] = email 
                session['user_id'] = current_user['user_id']

                if session['Logged_in']:
                    app.logger.info('session created!')
                flash('Account created', 'success')
                return redirect(url_for('home'))
            else:
                flash('Password do not match', 'danger')
                return redirect(url_for('login'))
        else:
            flash('No user found', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)

@app.route("/shop", methods=['GET', 'POST'])
def shop():
    return render_template('shop.html')

@app.route("/logout")
def logout():
    session.clear()
    flash('you are now logged out', 'success')
    return redirect(url_for('login'))

def findksimilarusers(user_id, ratings, metric = metric, k=k):
    similarities=[]
    indices=[]
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute') 
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[user_id-1, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
    print '{0} most similar users for User {1}:\n'.format(k,user_id)
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i]+1 == user_id:
            continue;

        else:
            print '{0}: User {1}, with similarity of {2}'.format(i, indices.flatten()[i]+1, similarities.flatten()[i])
            
    return similarities,indices

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

if __name__ == '__main__':
    app.run(debug=True)
