### Code Design

- Extensible.
- Single token (single word / punctuation) transforms run in one pass of source string.
  - Individual functions for each type of transform. Reference hash map for key-value transforms.
  - Default to running all transforms at once, option to run single transform.
- TODO: Other categories of transformations that can be grouped together to run in one pass? 

### UI

- Command line with flags.
- Default will run all transforms.
- Maybe gate round-trip machine translation behind a flag.
  - Download argos models for offline translation if flag set.
  - Option to use other translation APIs.
  - Google/bing translate support with warning.
- Interactive Y/N/add-to-dict prompts for unknown/uncommon words or autocorrect ambiguities.

### Verify Output
- Test text output against available Stylometry libs (e.g. Jstylo)