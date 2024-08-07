# TikTok API Guide

This guide will walk you through how to use the EnsembleData API to fetch data from TikTok. We'll cover how to fetch posts, users, comments, music, and more. Make sure to first check out the `Setup` section below to get setup with ensembledata's python library, which we'll use for fetching data throughout the guide.

## Table of Contents

[Setup](#setup) <br>
[Monitoring Hashtags](#monitoring-hashtags) <br>
[Monitoring Keywords](#monitoring-users) <br>
[User Details](#monitoring-users) <br>
[User Posts](#monitoring-users) <br>
[User Followers](#monitoring-users) <br>
[Post Details](#monitoring-users) <br>
[Post Comments](#monitoring-users) <br>
[Music](#monitoring-users) <br>

Extras: <br>
[What is a cursor?](#what-is-a-cursor) <br>


## Setup

(Optional) Create a virtual environment to run your python code in. <br>
This is not required, but keeps this project's dependencies separate from your other projects by installing them locally instead of globally.
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the `ensembledata` python package, which we'll later use to fetch data from the EnsembleData API.
```bash
pip install ensembledata
```

Create an EnsembleData Client by passing in your API token. <br>
If you haven't got an API token, grab one for free by [creating an account](https://dashboard.ensembledata.com/) on our platform.
```python
from ensembledata.api import EDClient

client = EDClient("INSERT API TOKEN")
```

... and you're all ready to go! Let's dive into what you can do with the TikTok API.

## Monitoring Hashtags

There are two endpoints you can use to find TikTok posts using a specific hashtag. The first is the `Hashtag Search` which takes two parameters, a `hashtag` and a `cursor` [(What is a cursor?)](#cursors) and returns a list of about 20 posts.

Let's find some posts that use the hashtag `magic`.

```python
result = client.tiktok.hashtag_search(hashtag="magic", cursor=0)
posts = result.data["data"]

# Take a look at the first post
# print(posts[0])

print("Number of posts:", len(posts))
next_cursor = result.data.get("nextCursor")
```

To get the next batch of posts, we'll call the API again but this time with the next cursor value we got from the last request.

```python
result = client.tiktok.hashtag_search(hashtag="magic", cursor=next_cursor)
posts = result.data["data"]
next_cursor = result.data.get("nextCursor")
```

You can continue this process until you've fetched all the available posts for this hashtag. You'll know you've fetched all the posts once there is no 'nextCursor' in the response. 

The maximum number of posts you can fetch for a given hashtag varies depending on the popularity of the hashtag. Very popular hashtags tend to have a maximum of **4000-5000 posts**, while some hashtags may not have any posts at all.

### Automatic Cursor Handling

The second endpoint is the `Full Hashtag Search`, whose functionality is a lot like it sounds. It fetches all the posts available for a given hashtag in one go. Under the hood, it uses the same `Hashtag Search` endpoint we used above, but it handles the cursor for you. Let's take a look.

```python
result = client.tiktok.full_hashtag_search(hashtag="magic")
posts = result.data["data"]
```

That easy! This endpoint provides two extra parameters we can use to configure the request. The first is the `max_cursor` which we can use to tell the API to stop fetching posts after a certain cursor value and the second is the `days` parameter, which we can use to filter out posts older than the specified number of days.

Here we are fetching the first 2000 posts that use the hashtag `magic` and at most 7 days old.

```python
result = client.tiktok.full_hashtag_search(hashtag="magic", max_cursor=2_000, days=7)
posts = result.data["data"]
```













## Monitoring Keywords

### Manual Pagination
### Automatic Pagination

## TikTok User Posts

### From secuid
### From username

## TikTok User Info

### From secuid
### From username
### User liked posts

## TikTok User Followers

### Followers
### Followings

## TikTok Post Info

### Single Post
### Multiple Posts

## Post Comments

### Comments
### Replies


## Music

## Find music with keyword
## Find posts using music
## Music Info




## What is a cursor?

So you don't know what a cursor is? Fear not, we've got you covered.

Many APIs include endpoints that allow you to fetch items from a list, however, they often don't return all the items at once. Instead, they return a chunk of items from the list and send you back a cursor. 

The cursor is like a bookmark, it tells us where we're up to, or how far we are through the list of items. When we want to get the next chunk of items from the list we send the cursor with our next request to the API, so that it knows where to get the next chunk of items from.

Imagine the API we're using has information on 100 books. We want to fetch this data, so we make a request to get the books:

```python
result = api.get_books()
print(result.data)
```

Let's take a look at what the api responded with:

```python
{
    "data": [
        {"title": "Book 1", ...},
        {"title": "Book 2", ...},
        ...
        {"title": "Book 20", ...},
    ],
    "nextCursor": 20
}
```

Interesting, it only sent us the first 20 books, but it did also send us a `nextCursor`.

Let's use the `nextCursor` to get more books.

```python
result = api.get_books(cursor=20)
print(result.data)
```

```python
{
    "data": [
        {"title": "Book 21", ...},
        {"title": "Book 22", ...},
        ...
        {"title": "Book 40", ...},
    ],
    "nextCursor": 40
}
```

Great, it sent us the next 20 books, and another `nextCursor` we can use to get more books.

Viola, this is how you can use a cursor to iterate over a list of items via API.








