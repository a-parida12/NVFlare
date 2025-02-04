# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from argparse import Namespace
from typing import List

import pytest

from nvflare.private.fed.server.job_cmds import _create_list_job_cmd_parser

TEST_CASES = [
    (["-d", "-u", "12345", "-n", "hello_", "-m", "3"], Namespace(u=True, d=True, job_id="12345", m=3, n="hello_")),
    (["12345", "-d", "-u", "-n", "hello_", "-m", "3"], Namespace(u=True, d=True, job_id="12345", m=3, n="hello_")),
    (["-d", "-u", "-n", "hello_", "-m", "3"], Namespace(u=True, d=True, job_id=None, m=3, n="hello_")),
    (["-u", "-n", "hello_", "-m", "5"], Namespace(u=True, d=False, job_id=None, m=5, n="hello_")),
    (["-u"], Namespace(u=True, d=False, job_id=None, m=None, n=None)),
    (["nvflare"], Namespace(u=False, d=False, job_id="nvflare", m=None, n=None)),
]


class TestListJobCmdParser:
    @pytest.mark.parametrize("args, expected_args", TEST_CASES)
    def test_parse_args(self, args: List[str], expected_args):
        parser = _create_list_job_cmd_parser()
        parsed_args = parser.parse_args(args)
        assert parsed_args == expected_args
