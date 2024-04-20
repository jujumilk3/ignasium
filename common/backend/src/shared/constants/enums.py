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
