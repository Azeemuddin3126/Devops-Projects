echo "adding files......."
sleep 1
git add .
sleep 1

echo "commit"
read -p "Enter a commit msg: " cmt_msg 
git commit -m "$cmt_msg" 
echo "committed............"
sleep 1

echo "pushing to repo.............."
git push
echo "Completed!!!"
