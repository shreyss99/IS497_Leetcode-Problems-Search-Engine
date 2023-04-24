from django.shortcuts import render
from LC_SearchEngine.database import get_data

leetcode_problems = [
    {
        "problem_id": 1,
        "title": "Two Sum",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such "
                       "that they add up to target. You may assume that each input would have exactly one solution, "
                       "and you may not use the same element twice. You can return the answer in any order.",
        "is_premium": 0,
        "difficulty": "easy",
        "solution_link": "/articles/two-sum",
        "acceptance_rate": 46.7,
        "frequency": 100.0,
        "url": "https://leetcode.com/problems/two-sum",
        "discuss_count": 999,
        "accepted": "4.1M",
        "submissions": "8.7M",
        "companies": "Amazon,Google,Apple,Adobe,Microsoft,Bloomberg,Facebook,Oracle,Uber,Expedia,Twitter,Nagarro,SAP,"
                     "Yahoo...",
        "related_topics": "Array,Hash Table",
        "likes": 20217,
        "dislikes": 712,
        "rating": 97,
        "asked_by_faang": 1,
        "similar_questions": "[3Sum, /problems/3sum/, Medium], [4Sum, /problems/4sum/, Medium], [Two Sum II - Input "
                             "array is sorte..."
    }
]


def home(request):
    context = {
        "lc_problem_details": leetcode_problems
    }
    return render(request, "LC_SearchEngine/home.html", context)


def about_us(request):
    return render(request, "LC_SearchEngine/about_us.html")


def data_view(request):
    lc = get_data()
    print(lc)
    context = {
        "lc_problem_details": leetcode_problems
    }
    return render(request, "LC_SearchEngine/data.html", context)

