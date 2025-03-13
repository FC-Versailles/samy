import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.parse


# GitHub repository where images are stored (raw URL format)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/FC-Versailles/samy/main/"

# Function to fetch images from GitHub
def load_image_from_github(filename):
    url = GITHUB_BASE_URL + filename
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"⚠️ Could not load image: {filename}")
        return None

image = load_image_from_github("pic.png")
if image:
    st.image(image, width=100)
# Title & Player Overview
st.title("Samy Baghdadi - 27 (FR)")
# Button linking to Transfermarkt profile
st.link_button("Transfermarkt Profile", "https://www.transfermarkt.fr/samy-baghdadi/profil/spieler/511454")

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.header("🔍 Key Insights")
st.markdown(
    """
    **Samy Baghdadi** is a **dynamic and versatile forward** who excels in **pressing, link-up play, and goal-scoring movements**.  
    His ability to combine **off-the-ball work rate** with **attacking efficiency** makes him a strong asset for teams looking to enhance their forward line.  

    ##### **Personality & Mentality 🏃‍♂️💨**  
    - **High work rate** – presses aggressively and contributes defensively.  
    - **Resilient and adaptable** – has played in different leagues and systems.  
    - **Team-oriented mindset** – involved in both build-up play and goal-scoring opportunities.  

    ##### **Football Profile 🎯**  
    - **Pressing & Defensive Contribution:** Strong (high possession-adjusted pressures).  
    - **Link-Up Play & Passing:** Effective in combination play, supports build-up.  
    - **Finishing & xG Output:** Good shot selection but **room for improvement in conversion rate**.  
    - **Speed & Movement:** Agile, quick in transition, and makes intelligent runs behind defenses.  

    ##### **Best Suited For**  
    ✅ **High-intensity pressing teams** (Saudi Pro League , or MLS).  
    ✅ **Teams that play direct attacking football**, focusing on transition speed.  
    ✅ **Clubs looking for a versatile forward** who can play as a **striker or wide forward**.  

    **Samy Baghdadi is at the perfect moment to take a step up**, and his skill set makes him an **ideal candidate for an ambitious club** in a top-tier or competitive second-tier league. 🚀  
    """
)

# Define the WhatsApp number (include country code, no '+' sign)
whatsapp_number = "33771730001"  # Example: +33 for France

# Message to send
message = "Hello, I am interested in Samy Baghdadi . Can we discuss further?"

# Encode message for URL
encoded_message = urllib.parse.quote(message)

# WhatsApp URL
whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

# Button to open WhatsApp chat
if st.button("📲 Contact Sport Director"):
    st.markdown(f'<a href="{whatsapp_url}" target="_blank">Send a whatsapp</a>', unsafe_allow_html=True)


st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Vertical Display with Expanders
with st.expander("👤 Player Career | Looking for an International Project"):
    image = load_image_from_github("fiche.png")
    if image:
        st.image(image, use_container_width=True)
    
    st.markdown(
        """
        ### **Why It’s Time for Him to Play Abroad Again**  

        #### **🏆 Peak Years (26-29) Age Bracket)**  
        - At **27 years old**, he is at his **physical and technical peak**.  
        - If he wants a **bigger challenge**, now is the time before his prime years fade.  

        #### **🇫🇷 Proven Performance in France**  
        - He has performed well in the **Championnat National (3rd tier) and Ligue 2**.  
        - His **goal-scoring ability and versatility** (playing as a striker and winger) make him attractive for foreign clubs.  

        #### **📈 Need for Higher-Level Competition**  
        - Staying in **France’s 3rd division** limits exposure.  
        - Moving to a **stronger league (Belgium, Netherlands, or Portugal)** could help him elevate his game.  


        #### **💰 Increasing Market Value & Financial Benefits**  
        - A move abroad could significantly **boost his salary**. 
        - Many clubs outside France (**Middle East, MLS, or Belgium**) offer **better financial incentives**.  
        """
    )

with st.expander("📍 Position Played | Advanced N°10 or False 9"):
    image = load_image_from_github("position.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samy is a complete center offesnive player, he can play as number 10, contribute the game with his technical skills and passing habilities. He is also really good to play second striker, with high quality to move, reach the golden area and connect with striker. His quality of shooting shows that he can play as a striker")

with st.expander("⏳ Minutes played | A captain - Technical leadership"):
    image = load_image_from_github("minutes_played.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samy become a more and more important player within the team. He is now our captain.")

with st.expander("🛡 Player Profile | Mobile & technical finisher"):
    image = load_image_from_github("leaugue_Comparison.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samy is an offensive-minded forward or attacking midfielder who is highly effective in both goal-scoring and playmaking. His ability to progress the ball, make key passes, and pressure the opposition makes him an asset in attack. His playing style suggests he thrives in a possession-based, attacking team where he can receive the ball in advanced areas and contribute to finishing or assisting.")

with st.expander("⚽ Shot Map | Top Shooter"):
    image = load_image_from_github("Shot_map.png")
    if image:
        st.image(image, use_container_width=True)
    
    st.markdown(
        """
        **Key Statistics**  
        - **Expected Goals (xG):** 7.77  
        - **Actual Goals Scored:** 7 goals  
        - **Total Shots Taken:** 46 shots  
        - **Overperformance:** +2.35 goals (including 1 goal and 3 penalties)  
        - **xG per Shot (open play only):** 0.180  
        """
    )

with st.expander("📈 Performance Progression | more efficient and well-rounded attacker"):
    image = load_image_from_github("progression.png")
    if image:
            st.image(image, use_container_width=True)
        
    st.markdown(
            """
            This radar chart compares **Samy Baghdadi’s** performance across key metrics from the **2023/24 season (red)** to the **2024/25 season (blue)**.
    
            ### **Overall Analysis**  
            - **Samy has transformed into a more efficient and well-rounded attacker.**  
            - His **goal contributions, playmaking, and attacking involvement** have all improved.  
            - **Defensive contributions (pressing intensity) have dropped**, possibly due to a more advanced or specialized role.
            """
        )
with st.expander("👥 Player Comparison | Samy Baghdadi vs. Jonathan David"):
    image = load_image_from_github("radar.png")
    if image:
        st.image(image, use_container_width=True)
    
    st.markdown(
        """
        ### **Comparison: Samy Baghdadi vs. Jonathan David**  
        This radar chart compares **Samy Baghdadi (red)** to **Jonathan David (blue)**, a **first-division striker** (Lille OSC, Ligue 1).  
        The comparison provides insights into **how Samy stacks up against a proven top-flight forward**.

        ### **📊 What This Means for Samy Baghdadi’s Development**  
        🔹 **Samy is an effective pressing forward** with strong passing and build-up play.  
        🔹 **However, to compete at the first-division level, he needs to improve:**  

        - **xG and finishing ability** → Taking **higher-quality shots** and improving **conversion rate**.  
        - **Touches in the box & off-ball movements** → Finding **better positions for scoring chances**.  
        - **Dribbling and deep progressions** → Becoming **more dangerous in the final third**.  

        ### **🏆 Final Verdict: Ready for a Step Up?**  
        ✅ **Samy has first-division potential**, but he must **refine his attacking efficiency** to match a top-tier forward like **Jonathan David**.  
        ✅ A move to a **stronger league (Belgium, Netherlands, Portugal) or Ligue 2** could be the right transition before reaching the **top flight**.  
        """
    )


with st.expander("🏋️ Physical Performance | xxxx"):
    image = load_image_from_github("physique.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("xxxx")

with st.expander("🤕 Injury History | Samy"):
    image = load_image_from_github("injuries.png")
    if image:
        st.image(image, use_container_width=True)
    
    st.markdown(
        """
        **Samy has been fortunate to avoid any long-term injuries and has never missed a match due to injury.**  
        However, the performance team closely monitors his knee to ensure optimal condition and prevent potential issues.  

        For this reason, we have implemented an **individualized plan** for him, which includes:

        - **Training adaptation** to manage workload and reduce stress on the knee,  
        - **Prevention strategies** such as targeted exercises and recovery protocols,  
        - **Fitness development** to strengthen key areas and enhance durability.  

        This proactive approach helps Samy maintain peak performance while minimizing injury risks.
        """
    )

with st.expander("⚖️ Weight Evolution | Professional player"):
    image = load_image_from_github("poids.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Monitoring body composition is key to performance optimization. Samy cares about his weight and body fat")

with st.expander("🔥 Personnality & Motivation | Real passion for football & competitor"):
    image = load_image_from_github("Happiness.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Samy loves competition and fight for the win. He passionate about football and expect an interesting contract for his prime.")

with st.expander("📊 Game Report"):
    image = load_image_from_github("game_report.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Example of Game report, please contact Mathieu Feigean for more explanation or request.")






st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <p><strong>M.Feigean</strong> - Football Development</p>
    </div>
    """, unsafe_allow_html=True)

