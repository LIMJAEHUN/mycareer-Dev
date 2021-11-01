from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Admin페이지 사용설명서'),
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
                {
                    'title': _('NAVER PAGE'),
                    'url': 'https://www.naver.com/',
                    'external': True,
                },
                {
                    'title': _('채용담당자님들 채용글 업로드 방법'),
                    'url': 'https://www.naver.com/',
                    'external': True,
                },
            ],
            column=0,
            order=0
        ))

        self.children.append(modules.AppList(
            _('어플리케이션'),
            exclude=('auth.*',),
            column=0,
            order=0
        ))

        self.children.append(modules.RecentActions(
            _('최근 활동내역'),
            10,
            column=0,
            order=0
        ))

        self.children.append(modules.Feed(
            _('메이플스토리 공지사항'),
            feed_url='https://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fmaplestory.nexon.com%2FNews%2FNotice%2FAll&item=.news_board+li&item_desc=img+%40alt&item_date=dd&item_date_format=Y.m.d&max=5&order=document&guid=0',
            limit=20,
            column=0,
            order=0
        ))

        self.children.append(modules.Feed(
            _('메이플스토리 업데이트 뉴스'),
            feed_url='https://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fmaplestory.nexon.com%2FNews%2FUpdate&item=.update_board+li&item_date=dd&item_date_format=Y.m.d&max=5&order=document&guid=0',
            limit=20,
            column=0,
            order=0
        ))
