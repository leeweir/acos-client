# Copyright 2014,  Jeff Buttars,  A10 Networks.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import acos_client.v30.base as base

from persistence import CookiePersistence
from persistence import SourceIpPersistence
from ssl import ClientSSL
from ssl import ServerSSL
from httptemplate import Httptemplate, Httpurlhashtemplate, Tcptemplate, TcpProxyTemplate, ServerHealthcheckTemplate
from httptemplate import ConnectionReusetemplate


class Template(base.BaseV30):

    @property
    def client_ssl(self):
        return ClientSSL(self.client)

    @property
    def cookie_persistence(self):
        return CookiePersistence(self.client)

    @property
    def src_ip_persistence(self):
        return SourceIpPersistence(self.client)

    @property
    def server_ssl(self):
        return ServerSSL(self.client)

    @property
    def http_template(self):
        return Httptemplate(self.client)

    @property
    def http_connection_reuse_template(self):
        return ConnectionReusetemplate(self.client)

    @property
    def http_urlhash_template(self):
        return Httpurlhashtemplate(self.client)

    @property
    def tcp_template(self):
        return Tcptemplate(self.client)

    @property
    def tcp_proxy_template(self):
        return TcpProxyTemplate(self.client)

    @property
    def server_healthcheck_template(self):
        return ServerHealthcheckTemplate(self.client)

