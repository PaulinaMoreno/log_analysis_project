#!/usr/bin/python
import datetime
import psycopg2
DBNAME = "news"


def popular_articles():

    popular_articles = []
    try:
        conn = psycopg2.connect(database=DBNAME)
    except:
        print("I am unable to connect to the database.")
    cur = conn.cursor()
    sql = """
        SELECT title, views FROM articles, most_accessed
        WHERE path = concat('/article/',slug) order by views desc;"""
    cur.execute(sql)
    popular_articles = cur.fetchall()
    conn.close()
    return popular_articles


def popular_authors():

    popular_authors = []
    sql = """
        SELECT ath.name, sum(most.views) as total_views
        FROM authors as ath, articles as art, most_accessed as most
        WHERE ath.id = art.author and path = concat('/article/',slug)
        group by ath.id order by total_views desc; """
    try:
        conn = psycopg2.connect(database=DBNAME)
    except:
        print("I am unable to connect to the database.")
    cur = conn.cursor()
    cur.execute(sql)
    popular_authors = cur.fetchall()
    conn.close()
    return popular_authors


def perc_errors():

    perc_errors = []
    sql = """
        SELECT  to_char(total.log_date,'MONTH DD, YYYY') as f_date,
        round(error_request.n_errors * 100.0 / total.n_request,2) as percentage
        FROM (SELECT time::date as log_date, count(status) as n_request
        FROM log  group by log_date order by log_date desc) as total,
        (SELECT time::date as log_date, count(status) as n_errors
        FROM log WHERE status = '404 NOT FOUND'
        group by log_date order by log_date desc) as error_request
        WHERE total.log_date = error_request.log_date
        and (error_request.n_errors * 100.0 / total.n_request) > 1; """
    try:
        conn = psycopg2.connect(database=DBNAME)
    except:
        print("I am unable to connect to the database.")
    cur = conn.cursor()
    cur.execute(sql)
    perc_errors = cur.fetchall()
    conn.close()
    return perc_errors
