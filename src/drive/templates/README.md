## Agent templates

Currently only one template agent is available called `master` which job is to take
input from the user and dispatch work to other agents.

## Topic naming convention

The kafka topics should adhere to a naming convention similar to this (this is up ofcourse up 
to you if you want to manage your kafka topics in a different manner, but this is a recommendation):

**Consumer topics**:
- "drive.\<sender>.\<receiver>.query"
- "drive.\<receiver>.\<sender>.response"

**Producer topics**:
- "drive.\<receiver>.\<sender>.response",
- "drive.\<sender>.\<receiver>.query"

### Example

For example with two agents available called `master` and `searcher`, the topic
config for the **master** agent could look like:

**Consumer topics**:
- "drive.user.master.query"
- "drive.master.searcher.response"

**Producer topics**:
- "drive.user.master.response"
- "drive.master.searcher.query"

and the config for the **searcher** agent could look like:

**Consumer topics**:
- "drive.user.searcher.query"
- "drive.master.searcher.query"

**Producer topics**:
- "drive.user.searcher.response"
- "drive.master.searcher.response"
