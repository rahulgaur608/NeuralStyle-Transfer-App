#!/bin/bash
echo "Pushing changes to your GitHub profile repository..."
cd "$(dirname "$0")/rahulgaur608"
git push origin master
echo "Script completed. Check the output above to see if all changes were pushed successfully."
