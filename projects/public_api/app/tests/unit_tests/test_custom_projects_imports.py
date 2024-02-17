from shared.constants.enums import BlogParentPlatforms


def test_apex_blog_platforms():
    assert len(BlogParentPlatforms) > 0
    is_checked_github_included = False
    for platform in BlogParentPlatforms:
        if platform == "github":
            is_checked_github_included = True
    assert is_checked_github_included
