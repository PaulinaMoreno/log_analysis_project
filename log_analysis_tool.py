from log_db import popular_articles, popular_authors, perc_errors
from time import sleep
import operator


def main():
    print("_________________Log Analysis Tool____________________________")
    print("\n Request information from news database ...")
    sleep(3)
    print("\n ---------------------------------------------------------------")
    print("\n 1- What are the most popular three articles of all time?")
    rs_q1 = dict([(title, int(views))for title, views in popular_articles()])
    for key, value in sorted(rs_q1.items(), key=lambda x: x[1], reverse=True):
        print("\n Article: {:} - {:} views ".format(key, value))

    print("\n ---------------------------------------------------------------")
    print("\n 2- Who are the most popular article authors of all time?")
    rs_q2 = dict([(name, int(total_views))for name, total_views in
                 popular_authors()])
    for key, value in sorted(rs_q2.items(), key=lambda x: x[1], reverse=True):
        print("\n Author: {:} - {:} views ".format(key, value))

    print("\n ---------------------------------------------------------------")
    print("\n 3- On which days did more than 1% of requests lead to errors?")
    rs_q3 = dict([(date_day, percentage) for date_day, percentage
                 in perc_errors()])
    for key, value in sorted(rs_q3.items(), key=lambda x: x[1], reverse=True):
        print("\n Date: {:} - {:} '%'error ".format(key, value))

if __name__ == '__main__':
    main()
