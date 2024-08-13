# TikTok API Guide

This guide will walk you through how to use the EnsembleData API to fetch data from TikTok. We'll cover how to fetch posts, users, comments, music, and more. Make sure to first check out the `Setup` section below to get setup with ensembledata's python library, which we'll use for fetching data throughout the guide.

## Table of Contents

[Setup](#setup-) <br>
[Monitoring Hashtags](#monitoring-hashtags-) <br>
[Monitoring Keywords](#monitoring-keywords-) <br>
[User Info](#users-info-) <br>
[User Posts](#user-posts-) <br>
[User Followers](#user-followers-) <br>
[Post Info](#post-info-) <br>
[Post Comments](#post-comments-) <br>
[Music](#music-) <br>

Extras 📚 <br>
[What is a cursor?](#what-is-a-cursor) <br>


## Setup 🛠️

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

<br>
<br>

## Monitoring Hashtags ✨

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

> For more details on the Hashtag Search endpoint, check out the [Hashtag Search API docs](https://ensembledata.com/apis/docs#tag/Tiktok/operation/full_search_hashtag_tt_hashtag_recent_posts_get).

### Automatic Cursor Handling

The second endpoint is the `Full Hashtag Search`, whose functionality is a lot like it sounds. It fetches all the posts available for a given hashtag in one go. Under the hood, it uses the same `Hashtag Search` endpoint we used above, but it handles the cursor for you. Let's take a look.

```python
result = client.tiktok.full_hashtag_search(hashtag="magic")
posts = result.data["data"]
```

That easy! This endpoint provides two extra parameters we can use to configure the request. The first is the `max_cursor` which we can use to tell the API to stop fetching posts after a certain cursor value and the second is the `days` parameter, which we can use to filter out posts older than the specified number of days.

Here we are fetching those that use the hashtag `magic` and are at most 7 days old within the first 2000 posts.

```python
result = client.tiktok.full_hashtag_search(hashtag="magic", max_cursor=2_000, days=7)
posts = result.data["data"]
```

> For more details on the Full Hashtag Search endpoint, check out the [Full Hashtag Search API docs](https://ensembledata.com/apis/docs#tag/Tiktok/operation/full_search_hashtag_tt_hashtag_recent_posts_get).

<br>
<br>

## Monitoring Keywords ✨

### Manual Pagination
### Automatic Pagination

## User Posts ✨



### From secuid
### From username

<br>
<br>

## User Info ✨

There are a few different ways we can get TikTok user information via the API. Similarly to when fetching user posts, we need to provide either a `username` or a `sec_uid` (secondary user id).

Here's just some of the key information you can find with the user info endpoints:

- region
- nickname
- username
- total likes
- followers
- number of posts
- bio / signature
- verified status
- profile picture


> You'll also find the `uid` (user id) and the `sec_uid` (secondary user id) which you may need for fetching data from other endpoints.


To see all the available information, head over to the documentation for the following endpoints and check out the response samples in the right panel.

### User Info from Username

[View Documentation](https://ensembledata.com/apis/docs#tag/Tiktok/operation/tiktok_user_info_from_username)


```python
result = client.tiktok.user_info_from_username(
    username="zachking"
)
```

### User Info from Secuid

[View Documenation](https://ensembledata.com/apis/docs#tag/Tiktok/operation/tiktok_user_info_from_secuid)

<!-- TODO: Talk about what else is available with alternative method -->

```python
result = client.tiktok.user_info_from_secuid(
    sec_uid="MS4wLjABAAA..."
)

user = result.data["user"]
print("Username:", user["unique_id"])
print("Nickname:", user["nickname"])
print("Followers:", user["follower_count"])
print("Posts:", user["aweme_count"])
print("Likes:", user["total_favorited"])
```

 The `user_info_from_secuid` endpoint has an optional `alternative_method` parameter, which when set to `True` will send back a different payload which contains some different information. There is a lot of overlap between the different responses for `alternative_method=True` and `alternative_method=False`, but each contain some information the other does not. For example, `alternative_method=True` gives you information about the account's category.

### User Liked Posts

[View Documenation](https://ensembledata.com/apis/docs#tag/Tiktok/operation/tiktok_user_liked_posts)

If this information is publicly avaiable we can also fetch the posts that a user has liked. To do so we'll need the user's `sec_uid`.

```python
result = client.tiktok.user_liked_posts(
    sec_uid="MS4wLjABAAA...",
)
posts = result.data["liked_posts"]
next_cursor = result.data.get("nextCursor")
```

If the next cursor value is not null, we can fetch more posts by making another request likes so [(What is a cursor?)](#cursors).

```python
result = client.tiktok.user_liked_posts(
    sec_uid="MS4wLjABAAA...",
    cursor=next_cursor
)
more_posts = result.data["liked_posts"]
next_cursor = result.data.get("nextCursor")
```

<br>
<br>

## User Followers ✨

Now, let's dive into the data you can retreive around followers on TikTok.

### Followers

[Documentation](https://ensembledata.com/apis/docs#tag/Tiktok/operation/tiktok_user_followers)

Our TikTok Followers API allows you to retrieve a user's most recent 5000 followers, i.e the last 5000 people to follow this user. To do so we'll require both the the user id and the secondary user id.

```python
result = client.tiktok.user_followers(
    id="6784819479778378757",
    sec_uid="MS4wLjABAAAAQ45...",
)

followers = result.data["followers"]
follower_count = result.data["total"]
next_cursor = result.data["nextCursor"]
```

A single request will return 100 followers, to get more send another request, this time passing in the cursor value we got from the previous request ([What is a cursor?](#cursors)). Note: the maximum you can retrieve is 5000.

### Followings

[Documentation](https://ensembledata.com/apis/docs#tag/Tiktok/operation/tiktok_user_followings)

Additionally, you can fetch the 'followings', which are the people the user themself follows. This endpoint works very similarly to the endpoint to fetch followers:

```python
result = client.tiktok.user_followings(
    id="6784819479778378757",
    sec_uid="MS4wLjABAAAAQ45...",
)

followers = result.data["followings"]
follower_count = result.data["total"]
next_cursor = result.data.get("nextCursor")
next_page_token = result.data.get("nextPageToken")
```

A single request will return 100 followings. To get more you'll need to use the `cursor` AND the `page_token`. Let's see how we can get the next chunk of followings below:

```python
result = client.tiktok.user_followings(
    id="6784819479778378757",
    sec_uid="MS4wLjABAAAAQ45...",
    cursor=next_cursor,
    page_token=next_page_token,
)

next_cursor = result.data.get("nextCursor")
next_page_token = result.data.get("nextPageToken")
```

Easy! We successfully used the cursor to get more results. You can continue this process until there is no `nextCursor` or `nextPageToken` in the response, which indicates that there are no more retrievable results.

<br>
<br>

## Post Info ✨

Let's look at fetching the data for a post on TikTok. The most basic way to do this is using the `post_info` endpoint which we'll take a look at first.

Here's just some of the key information you can find with the post info endpoints:

- plays, likes, comments, downloads, shares, collects, forwards
- video url
- video cover
- post description
- hashtags
- music info
- language
- region
- author info



### Single Post

[Documentation](https://ensembledata.com/apis/docs#tag/Tiktok/operation/tiktok_post_info)

Here we just need to supply the url for the TikTok post. You can easily find this by navigating to the post in your browers and copying the page url from the search bar. It should look like what we seen in the example below:

```python
result = client.tiktok.post_info(
    url="https://www.tiktok.com/@daviddobrik/video/7165262254722534698",
)
post = result["data"][0]
author_data = post["author"]
music_data = post["music"]
post_desc = post["desc"]
likes = post["statistics"]["digg_count"]
plays = post["statistics"]["play_count"]
shares = post["statistics"]["share_count"]
comments = post["statistics"]["comment_count"]
```

### Multiple Posts

If need to fetch data for many TikTok posts at once, then this is the endpoint for you. For this endpoint you'll need to extract the post ids and pass them in as a list. Note that the endpoint accepts a maxium of 100 post ids at once. If more than 100 ids are supplied the API will return an error notifying you of this.

> You can either find the post ids via other endpoints or you can find them at the end of the post url as seen in the previous example.

```python
result = client.tiktok.multi_post_info(
    aweme_ids=[
        "7210531475052236078", 
        "7102806710334606597", 
        "710280671033460623434597"
    ],
)
posts = result["data"]
```

<br>
<br>

## Post Comments ✨

### Comments
### Replies


<br>
<br>

## Music ✨

## Find music with keyword
## Find posts using music
## Music Info


<br>
<br>

## What is a cursor? 📚

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

### References

- [EnsembleData API Documentation](https://ensembledata.com/apis/docs)
- [EnsembleData TikTok API](https://ensembledata.com/tiktok-api)
- [EnsembleData TikTok Scraping Overview](https://ensembledata.com/tiktok-api/scraping-overview)
- [EnsembleData python package](https://github.com/ensembledata/ensembledata-python)






