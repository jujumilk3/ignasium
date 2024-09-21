from enum import Enum


class MyStringEnumMixin(str, Enum):
    def __str__(self):
        return self.value


class LangCode(MyStringEnumMixin):
    KOREAN = "ko"
    ENGLISH_US = "en-US"


class BlogParentPlatforms(MyStringEnumMixin):
    GITHUB = "github"
    AWS = "aws"
    BLOOMBERG = "bloomberg"
    GOOGLE = "google"
    MICROSOFT = "microsoft"
    META = "meta"
    NETFLIX = "netflix"
    REDHAT = "redhat"
    TWITTER = "twitter"
    UBER = "uber"
    YAHOO = "yahoo"
    ATLASSIAN = "atlassian"
    NAVER = "naver"
    KAKAO = "kakao"


class TechBlogAddresses(MyStringEnumMixin):
    GITHUB = "https://github.blog/"
    AWS = "https://aws.amazon.com/blogs/"
    BLOOMBERG = "https://www.techatbloomberg.com/"
    GOOGLE = "https://developers.googleblog.com/"
    MICROSOFT = "https://devblogs.microsoft.com/"
    META = "https://about.fb.com/news/"
    NETFLIX = "https://netflixtechblog.com/"
    REDHAT = "https://www.redhat.com/en/blog"
    TWITTER = "https://blog.twitter.com/engineering/en_us.html"
    UBER = "https://eng.uber.com/"
    YAHOO = "https://yahooeng.tumblr.com/"
    ATLASSIAN = "https://www.atlassian.com/blog/engineering"
    NAVER = "https://d2.naver.com/home"
    KAKAO = "https://tech.kakao.com/"
