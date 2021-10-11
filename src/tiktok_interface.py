from base_interface import Interface_IH


class Tiktok_I_IH(Interface_IH):

	def get_posts_from_hashtag(self, hashtag, depth = 1):	
		"""Fetch list of most popular posts related to this hashtag 
		with information about users

		Args:
			hashtag (string): hashtag name
			depth (int, optional): [description]. Defaults to 1.

		Returns:
			[type]: [description]
		"""

		end_point = self.req_url+ '/tt/hashtag/posts'
		payload = {'name':hashtag, 'depth':depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r	

	def get_user_info(self, name):	
		"""Get profile information of a user	

		Args:
			name (string): username (a.k.a. handle)

		Returns:
			[type]: [description]
		"""        
		end_point = self.req_url+ '/tt/user/info'
		payload = {'username':name, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_user_posts(self, username, depth = 1):	
		end_point = self.req_url+ '/tt/user/posts'
		payload = {'username':username, 'depth': depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_user_posts_id(self, secUid, depth = 1):	
		end_point = self.req_url + "/tt/user/posts-from-id"
		payload = {'secUid':secUid, 'depth': depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_recent_posts_from_hashtag(self, hashtag, days = 10):	
		"""Fetch list of recent posts (using the hashtag name) with information 
		about users.

		Args:
			hashtag (string): hashtag name
			days (int, optional): number of last days to retrieve. Defaults to 10.

		Returns:
			dictionary: content of the response, None if it failed
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/tt/hashtag/recent-posts'
		payload = {'name':hashtag, 'days':days, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r     

	def get_post_from_keyword(self, keyword, period = 0, sorting = 0, cursor = 0):	
		end_point = self.req_url+ '/tt/keyword/search'
		payload = {'name':keyword, 'period':period, "sorting":sorting, "cursor":cursor, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r  

	def get_comments(self, aweme_id, cursor = 0):	
		end_point = self.req_url+ '/tt/post/comments'
		payload = {"aweme_id":aweme_id, "cursor":cursor, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r  

	def get_comment_replies(self, aweme_id, comment_id, cursor = 0):	
		end_point = self.req_url+ '/tt/post/comments'
		payload = {"aweme_id":aweme_id, "comment_id":comment_id, "cursor":cursor, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r  