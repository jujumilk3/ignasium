import requests
from bs4 import BeautifulSoup

# GitHub 블로그 URL
BLOG_URL = "https://github.blog/"


if __name__ == "__main__":
    pass
    # crawl_github_blog()
    test_url = "https://github.blog/engineering/engineering-principles/how-github-supports-neurodiverse-employees-and-how-your-company-can-too/"
    response = requests.get(test_url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")

    # 본문 추출 (GitHub 블로그 구조에 따라 필요한 태그 변경 가능)
    # find by css selector
    article_content = soup.select_one("main#start-of-content")
    print("-----")
    print("article_content", article_content)
    print("-----")
