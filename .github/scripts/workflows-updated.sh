if [ "$(git diff --stat HEAD -- .github/workflows/)" ]; then
    echo "Updates to workflows detected.";
    echo ::set-output name=workflow_updated::true;
    cat << EOF > temp-issue-template.md;
---
title: Manual Update to Files from Cookiecutter Needed
labels: automated issue, maintenance
---
The template from the Cookiecutter which created this project must be updated using Cruft.

Normally this is an automated process, but the current updates include changes to the
Github Actions workflow files, and Github Actions does not allow those to be updated
by another workflow.

Run \`cruft update -s\` then manually review and update the changes, before pushing a PR
for this.
EOF
else
  echo "No updates to workflows.";
  echo ::set-output name=workflow_updated::false;
fi;