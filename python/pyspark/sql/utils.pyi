#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pyspark import SparkContext as SparkContext  # noqa: F401
from typing import Any, Optional

class CapturedException(Exception):
    desc: Any = ...
    stackTrace: Any = ...
    cause: Any = ...
    def __init__(
        self, desc: Any, stackTrace: Any, cause: Optional[Any] = ...
    ) -> None: ...

class AnalysisException(CapturedException): ...
class ParseException(CapturedException): ...
class IllegalArgumentException(CapturedException): ...
class StreamingQueryException(CapturedException): ...
class QueryExecutionException(CapturedException): ...
class PythonException(CapturedException): ...
class UnknownException(CapturedException): ...

def convert_exception(e: Any): ...
def capture_sql_exception(f: Any): ...
def install_exception_handler() -> None: ...
def toJArray(gateway: Any, jtype: Any, arr: Any): ...
def require_test_compiled() -> None: ...

class ForeachBatchFunction:
    sql_ctx: Any = ...
    func: Any = ...
    def __init__(self, sql_ctx: Any, func: Any) -> None: ...
    error: Any = ...
    def call(self, jdf: Any, batch_id: Any) -> None: ...
    class Java:
        implements: Any = ...

def to_str(value: Any): ...
