echo creating ssh key using ed25519...........
sleep 1

read -p "Enter your github mail: " mail
ssh-keygen -t ed25519 -C $mail
echo creating key......
echo pls wait..........
sleep 1

echo evaluating key....
sleep 1
eval "$(ssh-agent -s)"
echo done.....
sleep 1

echo  adding .........
ssh-add ~/.ssh/id_ed25519
echo done
sleep 1

cat ~/.ssh/id_ed25519.pub
echo Done paste this in github key 
