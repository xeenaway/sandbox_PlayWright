from pytest import mark


categories = {'argnames': 'category',
              'argvalues': ['Getting Started', 'Friendly & Easy to Learn', 'Applications', 'Open-source',
                            'Latest News', 'Upcoming Events']}


@mark.parametrize(**categories)
def test_present_categories(desktop_app, category):
    desktop_app.navigate_to('About')
    assert desktop_app.about.check_category_exist(category)
