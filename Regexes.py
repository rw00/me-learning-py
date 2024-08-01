import re
def test_emails():
    pattern = re.compile(r"^[a-z0-9\.\-]+@[a-z]+\.(org|com)$")
    emails = ["joe.1@myblog.com", "py-list@python.org", "in{valid}`email`@test.com"]
