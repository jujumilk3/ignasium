from enum import Enum


class MyStringEnumMixin(str, Enum):
    def __str__(self):
        return self.value


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
