Please review the IAB Tech Lab Open Source Initiative Governance guidelines [here](http://iabtechlab.com/opensource) for contributing to this project.

# Executive Summary

This repository contains a list of human reviewed content and the labels assigned by those people according to the [GARM](https://wfanet.org/l/library/download/urn:uuid:7d484745-41cd-4cce-a1b9-a1b4e30928ea/garm+brand+safety+floor+suitability+framework+23+sept.pdf) standard.  The purpose of this repository is two fold.
1. Encourage research projects to better use technology to implement the GARM standard.
1. Encourage open debate about the implementation of the standard to highly variable UGC content.

# Format
Each type of content will have its own file to accommodate the specific nuances of that content type.  Each file will be a CSV file with double quotes to surround fields as necessary, and backlash to escape intrafield double quotes.

## Video
The video format will contain at least the following columns
1. `label` - Of the 11 GARM categories, the highest label applicable.  The label values are one of `minimal`, `low`, `medium`, `high`, or `floor`.  For example if a video is medium for adult content, high for weapons, minimal for everything else then the label would be high.
1. `url` - The URL where the video can be found.
1. `title` - The user supplied title of the video

Note that at least for the YouTube file, the distribution of labels is ***not*** indicative of the distribution of labels on the platform as a whole.  The distribution was chosen to give a more uniform set of labels.

### YouTube
YouTube videos will be hosted by YouTube.  The titles provided are those at the time of upload of the data file, however, titles on YouTube are mutable and may change in the future.  We cannot guarantee that the title in the file is the same as the current title.  In addition YouTube videos may be taken down by the platform at any time.  Should anyone come across a video which is broken please submit a pull request.

# Challenges
Should someone wish to challenge a particular please submit a pull request and mention the piece of content by both file, URL, and desired new label.  Please also submit a reason for why the label should change.  The uploader of the file will respond in kind and the following flow will commence.
1. An agreement that the label is wrong.  In this case the pull request is accepted with no further conversation is needed.
1. A disagreement, instead stating that the uploader thinks label is correct.
    1. The uploader will provide a reason why it is correct.
    1. If the challenger agrees, then the pull request is rejected and no change is made.
    1. If the challenger disagrees then the pull request remains open.
        1. The community at large will now be able to comment to convince either the challenger or uploader to change their mind.
        1. If this is successful then the pull request will be closed as desired
        1. If this is unsuccessful then the particular piece of content will be brought to the GARM committee for resolution.
        1. GARM will then either update their definitions to resolve the dispute or issue a ruling, in either fashion stating how to close the pull request.

# Evaluations
Code is provided to evaluate any dataset against one supplied in this directory.  For the most up to date usage of the evaluation code, simply run `python evaluation.py -h` to get the help.  In addition you can see an example output by running `python evaluation.py -l video/youtube.csv -p test/youtube-test.csv`.  Tests can be run with `python -m pytest`.
