if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/bakrapalan/AutoForwardBot.git /AutoForwardBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AutoForwardBot
fi
cd /AutoForwardBot
pip3 install -U -r requirements.txt
echo "Starting Bot This May Take Time Depending On Database Size..."
python3 bot.py
