# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class GetInstTransInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'GetInstTransInfo','retailcloud')

	def get_aliyunUid(self):
		return self.get_body_params().get('aliyunUid')

	def set_aliyunUid(self,aliyunUid):
		self.add_body_params('aliyunUid', aliyunUid)

	def get_aliyunEquipId(self):
		return self.get_body_params().get('aliyunEquipId')

	def set_aliyunEquipId(self,aliyunEquipId):
		self.add_body_params('aliyunEquipId', aliyunEquipId)

	def get_aliyunCommodityCode(self):
		return self.get_body_params().get('aliyunCommodityCode')

	def set_aliyunCommodityCode(self,aliyunCommodityCode):
		self.add_body_params('aliyunCommodityCode', aliyunCommodityCode)