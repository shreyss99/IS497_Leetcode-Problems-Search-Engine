from LC_SearchEngine.models import LeetcodeData


def get_data():
    return LeetcodeData.objects.all()
