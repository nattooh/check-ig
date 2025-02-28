from bs4 import BeautifulSoup

# Function to extract the usernames from HTML
def extract_names_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Find all <a> tags with 'href' attribute starting with 'https://www.instagram.com/'
        usernames = [a_tag['href'].split('/')[-1] for a_tag in soup.find_all('a', href=True) if 'https://www.instagram.com/' in a_tag['href']]
    
    return usernames

# Load your follower and following HTML files
followers = extract_names_from_html('followers_1.html')  # Replace with the actual file path
following = extract_names_from_html('following.html')  # Replace with the actual file path

# Convert lists to sets for easier comparison
followers_set = set(followers)
following_set = set(following)

# Identify who you don't follow and who doesn't follow you
dont_follow_back = followers_set - following_set
not_following_you = following_set - followers_set

# Print the results
print("People you don't follow back:", dont_follow_back)
print("People who don't follow you:", not_following_you)
