import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCOSystem.settings')

import django
django.setup()

from django.utils import timezone
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from signin.models import signup_model
from index.models import Posts
from my_profile_feed.models import user_profile, Notification, Address
from profiles.models import Follow

# all_profiles = user_profile.objects.all()
# author_profiles = [[ap.user_name, ap.user_email] for ap in all_profiles]

###########################################################################
# ALL POSTS LIST(i.e. lists of dictionaries of form [{ 'title': "...", 'text': "..."}])
###########################################################################

all_posts_list = [
    {
        "title": "How to prepare for GATE CSE – 2019" ,
        "text": """<p><strong>GATE</strong>(<strong>Graduate Aptitude Test in Engineering</strong>) is one the most important and in-demand entrance exam for engineering graduates in our country. M.Tech. in Computer Science is one of the most demanding courses at prestigious institutes like IISCs and IITs. GATE(Graduate Aptitude Test in Engineering) is one of the ways to get into these top institutes.<br />
                    Every year around 10 Lakh candidates apply for GATE exam and very few of them manage to ace the exam with good score. So the competition is clearly very tough and simply preparing without any strategy will make it difficult to land you into IISCs and IITs.</p>

                    <p><a href="http://geeksforgeeks.org/" rel="noopener" target="_blank">GeeksforGeeks&nbsp;</a>brings you a complete guide and preparation strategy to crack the&nbsp;<a href="https://www.geeksforgeeks.org/gate-cs-2019-important-dates-and-links/" rel="noopener" target="_blank">GATE CSE 2019</a>&nbsp;with flying rank. We&rsquo;ll guide you through out the whole course, from&nbsp;<em>starting your<a href="https://www.geeksforgeeks.org/gate-corner-2-gq/" rel="noopener" target="_blank">GATE preparation</a>&nbsp;</em>to&nbsp;<em>how to answer GATE questions</em>.</p>

                    <p><strong>Let us now concentrate on few Important points :</strong></p>

                    <ul>
                        <li><strong>Analyze GATE syllabus:</strong>&nbsp;Start with analyzing the&nbsp;<a href="https://www.geeksforgeeks.org/gate-cs-2019-syllabus/" rel="noopener" target="_blank">GATE syllabus</a>. Start divide and Conquer, try to break the syllabus into sub-categories and do the same with each subject further. It will help you to prioritize subjects and&nbsp;<a href="https://www.geeksforgeeks.org/important-topics-prepare-gate-2018-computer-science-paper/" rel="noopener" target="_blank">important topics</a>&nbsp;in each subject. After doing this, you will get a clear insight into where you stand and how far is left to cover. Analyzing syllabus will also help you to understand about the important subjects and pattern of GATE exam.</li>
                        <li><strong>Start preparing today :</strong>&nbsp;Time is like money, so spend it wisely. The best time to start your GATE preparation is today, just after completing this read. Just pick one of the subjects you feel good and start the preparation. You may start with some easy and scoring subjects like&nbsp;<a href="http://www.geeksforgeeks.org/dbms/" rel="noopener" target="_blank">DBMS</a>,&nbsp;<a href="https://www.geeksforgeeks.org/operating-systems/" rel="noopener" target="_blank">Operating Systems</a>&nbsp;or&nbsp;<a href="https://www.geeksforgeeks.org/computer-network-tutorials/" rel="noopener" target="_blank">Computer Networks</a>(totally depends on individual). After completing first subject and its GATE questions, you can immediately pick the second subject. As soon as two subjects are completely covered, you will start feeling more confident.<br />
                        After completing one subject, the immediately next task should be solving&nbsp;<a href="https://www.geeksforgeeks.org/gate-corner-2-gq/" rel="noopener" target="_blank"><strong>previously asked GATE questions</strong></a>&nbsp;of that subject. It will help you to uncover weak topics; try to recover those weak topics and resolve those questions.</li>
                        <li><strong>Follow a disciplined schedule :</strong>&nbsp;Make a schedule and follow it at any cost, literally. Decide a fixed number of hours for your GATE preparation and complete it daily; remember, consistency is a compulsion here. Maybe print a calendar from starting day to intended course completion day and stick it front of your study table. Every day you completed those hours, mark the date with green pen and do the same with red pen if you missed.</li>
                        <li><strong>Take running notes while studying:</strong>&nbsp;Note down the important points in notebook while covering the topics. It will definitely help you in revisions. Decide one day in a week to revise one of your previously completed subjects and use your&nbsp;<a href="https://www.geeksforgeeks.org/gate-cs-notes-gq/" rel="noopener" target="_blank">GATE notes</a>here.</li>
                        <li><strong>Subjects easy to score:</strong>&nbsp;There are few subjects which are easier to score, like&nbsp;<a href="https://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/" rel="noopener" target="_blank">Digital Logic</a>,&nbsp;<a href="https://www.geeksforgeeks.org/engineering-mathematics-tutorials/" rel="noopener" target="_blank">Mathematics</a>&nbsp;and&nbsp;<a href="https://www.geeksforgeeks.org/placements-gq/" rel="noopener" target="_blank">Aptitude</a>. These three subjects cover 25-28% of complete GATE paper. Try not to leave these subjects uncovered as they are high scoring and will help to boost your GATE AIR.</li>
                        <li><strong>Track your preparation periodically:</strong>&nbsp;Solve previous GATE question for each subject. It will help you to recall and revise the subjects. We highly recommend giving&nbsp;<a href="https://practice.geeksforgeeks.org/courses/sudo-gate" rel="noopener" target="_blank">Sudo GATE subject-wise Test series</a>&nbsp;since these tests are build on learning while solving approach.</li>
                        <li><strong>Revise and practice are keys to GATE:</strong>&nbsp;After completing each subject, start revising each subject thoroughly. Revise the subject then solve&nbsp;<a href="https://www.geeksforgeeks.org/gate-corner-2-gq/" rel="noopener" target="_blank">previous year GATE questions</a>and take&nbsp;<a href="https://practice.geeksforgeeks.org/courses/sudo-gate" rel="noopener" target="_blank">subject-wise tests</a>. Remember, the only keys to score good AIR is revise and practice more.</li>
                        <li><strong>Take Mock Tests:</strong>&nbsp;At this final stage of preparation, practicing quality questions before attempting actual GATE will boost your confidence and improve your problem-solving speed. GeeksforGeeks has specially designed&nbsp;<a href="https://practice.geeksforgeeks.org/courses/sudo-gate" rel="noopener" target="_blank">Sudo GATE Mock tests</a>, which will help in boosting your GATE score. Questions in these Mock Test resembles with GATE actual questions and will give the GATE aspirants trailer before the Film.</li>
                        <li><strong>Use short notes :</strong>&nbsp;At this crucial stage, don&rsquo;t try to read any new topic. Just use your&nbsp;<a href="https://www.geeksforgeeks.org/lmns-gq/" rel="noopener" target="_blank">Last Minutes Notes</a>&nbsp;to recall only key points in each subject. We highly recommend using these&nbsp;<a href="https://www.geeksforgeeks.org/lmns-gq/" rel="noopener" target="_blank"><strong>LMNs</strong></a>, specially designed for last minutes preparation.</li>
                    </ul>
                    """
    },
    {
       "title" : "6 Effective GRE Preparation Strategies",
       "text": """<p>Just as the SAT is a standard admissions requirement for undergraduate programs, the GRE General Test is required by graduate programs in most fields. The GRE is not specific to any academic discipline, but it does test your executive functioning skills. Your executive reasoning operates like the CEO of your brain, and the GRE test writers want to see how well that CEO performs in terms of analyzing data, solving problems, and thinking critically.</p>

        <p>Success in the GRE is dependent on your ability to prioritize the information presented to you and organize it in ways that allow you to problem-solve efficiently. The following GRE preparation tips will optimize your performance:</p>

        <h2>1. Read a lot of analytical non-fiction</h2>

        <p>Do you think you could lose weight without avoiding snacks that have more calories than actual nutritional benefits? Properly feeding the mind is based on the same principle, and the best prescription for the health of your GRE skills is a well-balanced diet of reading material.</p>

        <p>Spending time on GRE preparation will be too much of a chore if you don&rsquo;t engage with supplementary analytical non-fiction in your spare time. Studies show that students who ace the verbal section of the GRE are often philosophy or liberal arts majors, who become well-acquainted with many types of narratives and academic writing in their undergraduate coursework.</p>

        <p>Reading about subjects unrelated to your main areas of interest might not be your favorite leisure activity, but the effort will pay off. The GRE&#39;s reading passages require you to become a highly skilled reader of diverse materials, and students who are familiar with a wide variety of texts have a substantial advantage.&nbsp;&nbsp;</p>

        <h2>2. Adhere to a regular GRE study plan</h2>

        <p>The exact amount of study time necessary for optimal GRE scores varies from person to person, but all students must develop solid command of the test, and this usually takes at least three months of careful GRE preparation. If you have the luxury of extra time, five months would be even better. The most important thing is that you develop a structured study plan and stick to it.</p>

        <p>If you succeeded in your high school math courses and are already an avid reader, you might not need to prepare as much as test-takers with lesser aptitude in these areas, but your background can at best give you a head start. Do not become overconfident, and do not underestimate the GRE.</p>

        <p>Create a realistic daily schedule that designates time for each GRE section, and make sure you cover all of the territory. You are ultimately your own teacher and coach. Just like flossing your teeth regularly prevents inconvenient and costly dental problems, you must preemptively study to ensure a smooth performance on the day of the test.</p>

        <h2>3. Take practice tests</h2>

        <p>When it comes to taking the GRE, one of the major roadblocks is stress. While you may find each section to be manageable on its own, taking the whole test (3 hours and 45 minutes) in one sitting is like running a marathon. You must be prepared and make sure you exercise, stretch, and build your weekly GRE mileage over the span of a few months. Students with insufficient stamina risk low scores.</p>

        <p>Taking practice tests will also help you learn to pace yourself. These will serve as valuable baseline reference points, and taking practice tests is a great way to build testing endurance. Practicing the full GRE will help you develop a feel for the test&#39;s mental and physical demands, which will eventually allow you to work through the entire test confidently and effectively.</p>

        <p>Make sure to take your practice tests under conditions that are as close as possible to an actual GRE administration. You want your brain to become accustomed to taking the test in realistic scenarios.</p>

        <h2>4. Know your weaknesses</h2>

        <p>The areas you find most challenging on the GRE are probably the ones you dislike the most. If you&rsquo;re a math whizz and have no use for verbose writing on esoteric topics, you will probably find swimming through dense prose akin to a quagmire. Conversely, people who find integers and exponential properties tedious usually have to fight tooth and nail to get through math concepts.</p>

        <p>Knowing your weaknesses and how you can chip away at them will allow you to build a balanced pace of study. Do whatever it takes to structure your study plan so that you can target your weaknesses more effectively. It might be awful at first, but it will get less cumbersome.</p>

        <p>When it comes to areas in which you&rsquo;re comfortable, choose study materials that expand your skills and knowledge rather than exercises that are easy for you. The goal is to make yourself focus under the most challenging circumstances by working through material that you find weighty and difficult.</p>

        <h2>5. Chart your progress</h2>

        <p>In job interviews, prospective employers want evidence of how applicants have contributed to work projects. They always appreciate statistical, concrete proof of accomplishment (such as boosting the company&rsquo;s sales by 5% or cutting operational expenses in half).</p>

        <p>GRE prep can also benefit from clear benchmarks of performance. Charting your progress is an absolute necessity, because it will provide an overview of your score improvements and will objectively assess the effectiveness of your study techniques.</p>

        <p>Your metric for improvement should have a consistent set of criteria, and you should measure your progress on a weekly or even daily basis. Regular self-evaluation will illuminate your improvements for each question type and section, and by tracking your study regimen, you&rsquo;ll be able to fix any harmful patterns.</p>

        <h2>6. Trust your gut instinct</h2>

        <p>You&#39;ve probably confronted multiple-choice questions where you&#39;ve narrowed down the options but can&#39;t decide between two plausible answers. You&rsquo;ve analyzed the problem, gathered information, evaluated your choices, and boiled them down to two by process of elimination.</p>

        <p>&ldquo;Gut instinct&rdquo; can be a scary concept, since this is merely another way to describe intuition, or the ability to grasp something immediately without cognitive information. When you&rsquo;re taking the GRE, hedging your bets on a 50% success rate (when you&rsquo;ve reduced your answer choices to two) can be a bit unsettling. But if you have thoughtfully and purposefully learned the material and practiced the exercises, then trusting your gut can become a shortcut to making a rational decision.</p>

        <p>As long as you have prepared yourself well and are executing sound test-taking strategies, it&#39;s OK to trust your instinct and carry forward with your intuitive choice. Everyone does a great deal of processing in the subconscious mind, and your gut feeling can help you solve a problem when your conscious mind falters.</p>
        """
    },
    {
        "title": "Best GRE Study Material",
        "text": """<p>Picking up the right study material is a key stage in your GRE preparation process. There are tonnes of books and free online material available on the Internet, but a very few of them offer the content which can actually help you crack the GRE. Here are some good books and resources we&rsquo;ve found out through our research which can help you prepare well for GRE and get you a commendable score.</p>

        <p><img alt="ETS Official Guide" src="http://www.indiaeducation.net/imagesvr_ce/3606/ETS.jpg" style="height:234px; width:180px" /></p>

        <h3>&nbsp;<strong><em>1.&nbsp;</em><em>ETS Official Guide to the GRE Revised General Test</em></strong></h3>

        <p>&nbsp;This is a must have book for every GRE aspirant. Why? Because it is written by the makers of GRE itself! This book gives a comprehensive overview of GRE &ndash; exam pattern, structure, question types and comes with 4 practice tests as well (2 paper, 2 CD-based). The questions and practice papers are very much similar to what you&rsquo;ll encounter in the actual GRE. Additionally, the official guide also provides effective strategies for each section and certain question types that a student might find difficult. Thus, you must have this GRE Bible!</p>

        <p><img alt="Manhattan Prep" src="http://www.indiaeducation.net/imagesvr_ce/7734/manhattan.png" style="height:196px; width:269px" /></p>

        <h3><strong><em>2.&nbsp;</em><em>Manhattan Prep Set of 8 Strategy Guides</em></strong></h3>

        <p>&nbsp;The Manhattan Prep series is one of the most widely recommended books for GRE and why it shouldn&rsquo;t be! It&rsquo;s not a single book, it&rsquo;s a set of 8 books that cover every important topic in depth &ndash; Algebra, Number Properties, Fractions, Geometry, Word Problems, Quantitative Comparisons, Text Completion and Sentence Equivalence, Reading Comprehension and Analytical Writing. You can either buy all the books or some selective ones based on your needs. Additionally, you also get access to 6 practice tests when you buy any one of the books. These books do not focus on teaching you the usual tactics but rather on building a solid fundamental grasp through their effective explanations and a huge basket of practice problems. If money is not issue for you, burn every other book and buy this one!</p>

        <p>&nbsp;</p>

        <p><img alt="Magoosh GRE Prep" src="http://www.indiaeducation.net/imagesvr_ce/2877/magoosh.png" style="height:232px; width:179px" /></p>

        <h3><strong><em>3.&nbsp;</em><em>Magoosh GRE Prep</em></strong></h3>

        <p>&nbsp;<em>Magoosh.com</em>&nbsp;is a very effective tool if you want to prepare for the GRE on your own. This online GRE preparation website focuses on interactive learning through video tutorials and practice questions with a very user-friendly interface. It allows aspirants to choose personalized plans based on different factors such as costs and duration of preparation. Additionally, it provides several free resources in the form of eBooks and customized study plans. Students have been said to improve their GRE scores on an average by 5 points after learning through Magoosh. Thus, this is definitely a bang for your buck if you&rsquo;re planning to prepare for the GRE on your own and if you prefer online learning over books.</p>

        <p>&nbsp;</p>

        <p><img alt="Barron's GRE" src="http://www.indiaeducation.net/imagesvr_ce/7525/barrons.jpg" style="height:279px; width:214px" /></p>

        <h3><strong><em>4.&nbsp;</em><em>Barron&rsquo;s GRE</em></strong></h3>

        <p>&nbsp;One of the oldest publications to guide students for GRE preparation, Barron&rsquo;s has always kept its position consolidated as a widely sought book for GRE no matter how many other publications come and go by. Although the level of questions isn&rsquo;t challenging as the actual GRE, Barron&rsquo;s GRE provides extremely useful explanation strategies as well as a solid question bank to practice the fundamentals. This should definitely be in your shelf during the early stages of your preparation.</p>

        <p>&nbsp;</p>

        <p><img alt="Princeton Review" src="http://www.indiaeducation.net/imagesvr_ce/851/princeton.jpg" style="height:269px; width:208px" /></p>

        <h3><strong><em>5.&nbsp;</em><em>The Princeton Review, Cracking the new GRE</em></strong></h3>

        <p>&nbsp;Another very popular book, Princeton Review is widely acclaimed for its strategies to deal with the GRE Verbal Section and for students who find it difficult to deal with the GRE Quantitative section even on the basic level. That said, one of the major drawbacks of this book is the lack of practice problems. Nevertheless, this is a good resource to be referred to if you&rsquo;re finding it difficult to deal with any of the GRE sections even on the basic level. Also, this is a good book for you if you prefer learning through visual aids.</p>

        <p><img alt="Kaplan GRE" src="http://www.indiaeducation.net/imagesvr_ce/5408/kaplan.png" style="height:278px; width:214px" /></p>

        <p>&nbsp;</p>

        <h3><strong><em>6.&nbsp;</em><em>Kaplan New GRE Premier</em></strong></h3>

        <p>&nbsp;A giant and very popular company for standardized test preparation, Kaplan is a household name for GRE preparation worldwide. This book provides innovative explanations as well as numerous practice exercises on various concepts across all the GRE sections. The practice tests that come along with the book are said to be very close or even difficult than the actual GRE. However, it has also been criticized for its jumbled up strategy to deal with the vocabulary section. That said, you should definitely keep this book in your list if you are aiming to solve a large quantity of practice problems.</p>
        """
    },
    {
        "title": "Best GRE Study Material – Section Wise",
        "text": """<p>Although there are a number of books that don&rsquo;t make it to our top list, there are several of them that are specifically recommended for individual GRE sections. For a better and thorough preparation approach for the GRE, we&rsquo;ve compiled a list of best GRE books for individual sections we well.</p>

        <h3><strong><em>Best Books for GRE Quantitative Section</em></strong></h3>

        <p>1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Manhattan&nbsp; 5LB Book of Practice Problems</p>

        <p>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ETS Official GRE Quantitative Reasoning Practice Questions</p>

        <p>3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GRE Math Prep Course (Nova&rsquo;s GRE Prep Course)</p>

        <p>4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kaplan GRE Math Workbook</p>

        <p>&nbsp;</p>

        <h3><strong><em>Best Books for GRE Verbal Section</em></strong></h3>

        <p>1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ETS Official GRE Verbal Reasoning Practice Questions</p>

        <p>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GRE Verbal Grail &ndash; Aristotle Prep (Good for Reading Comprehension)</p>

        <p>3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kaplan GRE Verbal Workbook</p>

        <p>4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Manhattan 5LB Book of Practice Problems (Questions harder than the actual GRE)</p>

        <p><strong><em>&nbsp;</em></strong></p>

        <h3><strong><em>Best Books for GRE Analytical Writing Ability (AWA) Section</em></strong></h3>

        <p>1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Vibrant Publishers GRE Analytical Writing &ndash; Solutions to Real Essay Topics ( Books 1 and 2)</p>

        <p>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ETS Official Guide to the GRE Revised General Test</p>

        <p>&nbsp;</p>

        <h3><strong><em>Best Books to learn GRE Vocabulary</em></strong></h3>

        <p>1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Word Power Made Easy &ndash; Norman Lewis</p>

        <p>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Barron&rsquo;s 1100 Words You Need to Know</p>

        <p>3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Magoosh GRE Vocabulary eBook</p>

        <p>4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Manhattan 500 Essential Words for GRE and Manhattan 500 Advanced Words for GRE</p>
        """
    },
    {
        "title": "GATE Preparation Books for Mechanical Engineering (ME)",
        "text": """<p>Said to be the mother of engineering, Mechanical Engineering (ME) is the most favourite stream of the candidates participating in GATE. Around 2 lac candidates alone appear for this stream.&nbsp;Here are some GATE preparation books for the strategic pre</p>

        <p>paration of Mechanical Engineering-</p>

        <h4>Strength of Materials by SS Rattan</h4>

        <p><strong>Review:</strong></p>

        <ul>
        	<li>Strength of Materials by SS Ratan unravels all the complexities of the section with utter clarity keeping the bar as low as possible in a basic language with the optimum use of jargons and good quality.</li>
        	<li>Strength of Materials (SOM) is one the most important and toughest section in GATE Mechanical Engineering. If prepared well, it can be one of the most scoring sections in GATE 2019.</li>
        	<li>Majority of questions under SOM is from&nbsp;Stress &amp; Strain, SFD &amp; BMD and Bending Moment.</li>
        	<li>examples.</li>
        	<li>For GATE 2019 aspirants, this book is a must-buy.</li>
        </ul>

        <h4>Theory of Machines by RS Khurmi</h4>

        <p><strong>Review:</strong></p>

        <ul>
        	<li>Though a tough nut to crack, the section could be scoring too. But only if prepared strategically by a good book and RS Khurmi provides all the candidates require to crack GATE 2019 labyrinth.</li>
        	<li>Theory of Machines section requires candidates to implicate their arithmetical abilities and knowledge of Mechanical &amp; Kinematics.</li>
        	<li>Majority of questions test candidates&rsquo; in-depth knowledge of frame of reference and 3D Geometry.</li>
        </ul>

        <h4>Other Good Books For GATE 2019 Mechanical Engineering</h4>

        <p>Other Important Sections include Mechanical Vibration, Machine Design, Engineering &amp; Applied Thermodynamics, Fluid Mechanics &amp; Fluid Machines and Operation Research. Candidates are required to follow the mentioned books for the respective sections</p>

        <table>
        	<tbody>
        		<tr>
        			<th>GATE Preparation Books for Mechanical Engineering</th>
        			<th>Author</th>
        		</tr>
        		<tr>
        			<td>Mechanical Vibration</td>
        			<td>GK Grover</td>
        		</tr>
        		<tr>
        			<td>Design Of Machine Elements</td>
        			<td>VB Bhandari</td>
        		</tr>
        		<tr>
        			<td>Engineering Mechanics</td>
        			<td>SS Bhavikatti</td>
        		</tr>
        		<tr>
        			<td>Fluid Mechanics</td>
        			<td>RK Bansal</td>
        		</tr>
        		<tr>
        			<td>Heat &amp; Mass Transfer</td>
        			<td>PK Nag</td>
        		</tr>
        		<tr>
        			<td>Engineering Thermodynamics</td>
        			<td>Cengel &amp; Boles</td>
        		</tr>
        		<tr>
        			<td>Internal Combustion Engine</td>
        			<td>V Ganesan</td>
        		</tr>
        		<tr>
        			<td>Refrigeration &amp; Air Conditioning</td>
        			<td>CP Arora</td>
        		</tr>
        		<tr>
        			<td>Material Science</td>
        			<td>UC Jindal</td>
        		</tr>
        		<tr>
        			<td>Production Engineering</td>
        			<td>Amitabh Ghosh</td>
        		</tr>
        		<tr>
        			<td>Industrial Engineering</td>
        			<td>OP Khanna</td>
        		</tr>
        	</tbody>
        </table>
        """
    },
    {
        "title": "GATE Preparation Books for Computer Science (CSE)",
        "text": """<p>Booming IT Sector and uninterrupted job opportunities in the field of CS/IT, the branch has recently become the most chosen branch among all the tech geeks and code lovers.&nbsp;Here are some good and well-reviewed GATE preparation books for Computer Science, we have found out for you-</p>

        <table>
        	<tbody>
        		<tr>
        			<th>GATE Preparation Books for Computer Science</th>
        			<th>Author</th>
        		</tr>
        		<tr>
        			<td>Algorithms</td>
        			<td>Cormen</td>
        		</tr>
        		<tr>
        			<td>Operating System</td>
        			<td>Galvin</td>
        		</tr>
        		<tr>
        			<td>Theory of Computation</td>
        			<td>Ullman</td>
        		</tr>
        		<tr>
        			<td>Computer Networks</td>
        			<td>Tanenbaum</td>
        		</tr>
        		<tr>
        			<td>Computer Organisation</td>
        			<td>Carl Hamacher</td>
        		</tr>
        		<tr>
        			<td>Database System</td>
        			<td>Korth</td>
        		</tr>
        		<tr>
        			<td>Compiler Design</td>
        			<td>Aho &amp; Ull Man</td>
        		</tr>
        		<tr>
        			<td>Digital Logic</td>
        			<td>Morris Mano</td>
        		</tr>
        		<tr>
        			<td>Software Engineering</td>
        			<td>Pressman</td>
        		</tr>
        	</tbody>
        </table>
        """
    },
    {
        "title": "10 Best Python Books for Beginners and Advanced Programmers",
        "text": """<h2><strong>Best Python Books for Beginners</strong></h2>

        <h3><a href="http://geni.us/T3V4EWB"><strong>Python Crash Course</strong></a></h3>

        <p><a href="http://geni.us/T3V4EWB"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/python-crash-course-227x300.jpg" style="height:400px; width:303px" /></a></p>

        <p>&lsquo;Python Crash Course&rsquo; by Eric Matthews is a fast-paced and comprehensive introduction to Python language for beginners, who wish to learn Python programming and write useful programs. The book aims to get you up to speed fast enough and have you writing real programs in no time at all. This book is also for programmers who have a vague understanding of the language and wish to brush up their knowledge before trying their hands on Python programming. As you work through the book, you will learn the use of libraries and tools such as Numpy and matplotlib and work with data to create stunning visualizations. You will also learn about the idea behind 2d games and Web applications and how to create them.</p>

        <p>This 560 pages long book is majorly dissected into two parts. The first part of the book discusses the basics of Python programming and sheds lights on concepts such as dictionaries, lists, loops, and classes. You will understand the working of a Python program and learn how to write clean and readable code which creates interactive programs. The part ends with the topic of how to test your code before you add it to a project. The second part of the book follows a practical approach and will help you test your knowledge by presenting three different projects, an arcade game, a simple web application and data visualizations using Python&rsquo;s libraries.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/T3V4EWB">here</a>.</p>

        <h3><a href="http://geni.us/TAKPM"><strong>Head-First Python (2nd edition)</strong></a></h3>

        <p><a href="http://geni.us/TAKPM"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/headfirst-261x300.jpg" style="height:400px; width:348px" /></a></p>

        <p>&lsquo;Head-First Python&rsquo; by Paul Barry is a quick and easy fix for you if you wish to learn the basics of Python programming without having to slog through counterproductive tutorials and books. The book will help you in gaining a quick grasp of the fundamentals of Python programming and working with built-in functions and data structures. The book then moves to help you build your own web application, exception handling, data wrangling, and other concepts. Head first Python makes use of a visual format rather than a text-based approach, helping you to see and learn better.</p>

        <p>&nbsp;</p>

        <p>The author is Paul Barry, a lecturer at the Institute of Technology, Carlow, Ireland. Before entering the academic world, he worked for over a decade in the IT industry. He is the author of certain well-known programming books, such as Programming the Network with Perl, Head First Programming and Head First Python.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/TAKPM">here</a></p>

        <h3><a href="http://geni.us/XNd0BY"><strong>Learn Python the Hard Way (3rd&nbsp;Edition)</strong></a></h3>

        <p><a href="http://geni.us/XNd0BY"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/hard-way-231x300.jpg" style="height:400px; width:308px" /></a></p>

        <p>&lsquo;Learn Python the Hard Way&rsquo; by Zed A. Shaw (3rd Edition) is a collection of 52 perfectly collated exercises. You will have to read the code and type it precisely. Once typed, you will have to fix the mistakes in the code for a better understanding and watch the programs run. These exercises will help you understand the working of software, structure of a well-written program and how to avoid and find common mistakes in code using some tricks that professional programmers have up their sleeves.</p>

        <p>The book begins it all by helping you install a complete Python environment, which helps you in writing optimized code. The book then discusses various topics, such as basic mathematics, variables, strings, files, loops, program design, and data structures among many others. The book is ideal for beginners who wish to learn Python programming through the crux of the language. The author is Zed A. Shaw, who is the creator of the Hard Way series which includes books on C, Python and Ruby programming language.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/XNd0BY">here</a></p>

        <h3><a href="http://geni.us/dGGBg"><strong>Python Programming: An Introduction to Computer Science (3rdEdition)</strong></a></h3>

        <p><a href="http://geni.us/dGGBg"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/pythonprogramming-244x300.jpg" style="height:400px; width:325px" /></a></p>

        <p>&lsquo;Python Programming&rsquo; by John Zelle is the third edition of the original Python programming book published in 2004, the second edition of which was released in 2010. Instead of treating this book as a source to Python programming, it should be taken as an introduction to the art of programming. This book will introduce you to computer science, programming, and other concepts, only using Python language as the medium for beginners. The book will discuss its contents in a style that is most suitable for beginners, who will find the concepts in the book easy to understand and interesting.</p>

        <p>&nbsp;</p>

        <p>The third edition of this extremely successful book follows the path paved by the first edition and continues to test students through a time-tested approach while teaching introductory computer science. The most notable change in this edition is the removal of nearly every use of python eval() library and the addition of a section which discusses its negatives. The latest version also uses new graphic examples.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/dGGBg">here</a></p>

        <h2><strong>Free Python Books for Beginners</strong></h2>

        <h3><a href="http://greenteapress.com/wp/learning-with-python/"><strong>Learning with Python: How to Think Like a Computer Scientist</strong></a></h3>

        <p><a href="http://greenteapress.com/wp/learning-with-python/"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/how-to-think-223x300.jpg" style="height:400px; width:297px" /></a></p>

        <p>&lsquo;Learning with Python&rsquo; by Allen Downey, Jeff Elkner and Chris Meyers is an introduction to Python programming and using the language to create wonderful real-world programs. The book is divided into 20 sections and also includes a contributors list and a way forward. The initial sections discuss the basics of programming and what makes up a program. Then it moves on to basic Python concepts such as variables, functions, conditionals, fruitful functions and iteration. Towards the end, the book discusses the core concepts such as objects, inheritance, lists, stacks, queues, trees and debugging.</p>

        <p>The book is available for free in a variety of formats, which include PDF, Postscript, Gzipped Rar and HTML. Users are free to download and print these files as the book is licensed under the GNU Free Documentation License. The book has also been translated in Spanish, Italian, German and Czech, and available for download.</p>

        <p>You can download the book for free&nbsp;<a href="http://greenteapress.com/wp/learning-with-python/">here</a></p>

        <h3><a href="https://python.swaroopch.com/"><strong>A Byte of Python</strong></a></h3>

        <p>&lsquo;A Byte of Python&rsquo; by C.H. Swaroop is a free book on Python programming with an aim to guide the beginner audience to an understanding of the Python language. The book will discuss the Python 3 version majorly, but will also help you adapt to the older versions of the language. The book is available in over 26 languages including Turkish, Swedish, French, Chinese, German, Spanish, Russian, Ukrainian, Portuguese and Korean. The translations have been provided by active community members who vigorously work to keep the edits going on as the book is updated.</p>

        <p>The book initiates its approach with an introduction to what the book is about and what it demands from the readers concerning dedication. Then it describes Python and how it has emerged as one of the most powerful languages in the programming world. It then moves on to Python concepts and describes them in detail along with examples at every step. It culminates with how you can continue learning Python after reading this book and leaves you with a problem to solve, testing your skills even at the last step.</p>

        <p>You can download the book for free&nbsp;<a href="https://python.swaroopch.com/">here</a></p>

        <h2><strong>Best Python Books Advanced Programmers</strong></h2>

        <h3><a href="http://geni.us/DtbjZJ"><strong>Introduction to Machine Learning with Python: A Guide for Data Scientists</strong></a></h3>

        <p><a href="http://geni.us/aYmL"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/machine-learning-229x300.jpg" style="height:400px; width:305px" /></a></p>

        <p>Many commercial applications and projects have employed machine learning as an integral ingredient, and the number of applications doing so has only risen over the years. This book by Sarah Guido and Andreas C. Muller will teach you how to use Python programming language to build your own machine learning solutions. As the amount of data usage increases with the second, the limitation to machine learning applications is only our imagination.</p>

        <p>Throughout the course of this book, you will learn about the steps required to create a rich machine-learning application using Python and scikit-learn library. The book will introduce you to the fundamental concepts and uses of machine learning, before moving on to the pros and cons of popular machine learning algorithms. You will then learn about the advanced methods for model evaluation and the concept of pipelines, which is used for encapsulating your workflow and chaining models. In conclusion, the book will provide suggestions to help you improve your data science skills.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/aYmL">here</a></p>

        <h3><a href="http://geni.us/xA2PP"><strong>Fluent Python: Clear, Concise, and Effective Programming</strong></a></h3>

        <p><a href="http://geni.us/xA2PP"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/Fluent-Python-228x300.jpg" style="height:400px; width:304px" /></a></p>

        <p>&lsquo;Fluent Python&rsquo; by Luciano Ramalho will be your hands-on-guide that will help you learn how to write effective Python code by using the most neglected yet best features of the language. The author will take you through the features and libraries of the language, and will help you make the code shorter, faster and readable.</p>

        <p>The book covers various concepts including python data model, data structures, functions as objects, object-oriented idioms, control flow, and metaprogramming. Using this book, advanced Python programmers will learn about Python 3 and how to become proficient in this version of the language. The author is Luciano Ramalho, a Web Developer who has worked with some of the largest news portals in Brazil using Python and has his own Python training company.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/xA2PP">here</a></p>

        <h3><a href="http://geni.us/yAoO1S"><strong>Python Cookbook: Recipes for Mastering Python 3</strong></a></h3>

        <p><a href="http://geni.us/yAoO1S"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/cookbook-229x300.jpg" style="height:400px; width:305px" /></a></p>

        <p>&lsquo;Python Cookbook&rsquo; by David Beazley and Brian K. Jones will help you master your programming skills in Python 3 or help you update older Python 2 code. This cookbook is filled with recipes tried and tested with Python 3.3 is the ticket for experienced Python programmers who wish to take the approach to modern tools and idioms rather than just standard coding. The book has complete recipes for a variety of topics, covering Python language and its uses, along with tasks common to a large number of application domains.</p>

        <p>Some of the topics covered in the book are but not limited to strings, data structures, iterators, functions, classes, modules, packages, concurrency, testing, debugging and exceptions. Throughout the book, the recipes mentioned above will presuppose that you have the necessary knowledge to understand the topics in the book. Each recipe contains sample code the reader can use in their projects. The code is followed by a discussion about the working of the code and why the solution works.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/yAoO1S">here</a></p>

        <h3><a href="http://geni.us/YWSzZ"><strong>Programming Python: Powerful Object-Oriented Programming</strong></a></h3>

        <p><a href="http://geni.us/YWSzZ"><img alt="" src="https://hackr.io/blog/wp-content/uploads/2018/12/programming-python-229x300.jpg" style="height:400px; width:305px" /></a></p>

        <p>&lsquo;Programming Python&rsquo; by Mark Lutz is ideal for programmers who have understood the fundamentals of Python programming and ready to learn how to use their skills to get real work done. This book includes in-depth tutorials on various application domains of Python, such as GUIs, the Web and system administration. The book will also discuss how the language is used in databases, text processing, front-end scripting layers, networking and much more.</p>

        <p>The book will explain the commonly used tools, language syntax, and programming techniques through a brief yet clear approach. The book is filled with many examples that show the correct usage and common idioms. The book also digs into the language as a software development tool, along with multiple examples illustrated particularly for that purpose.</p>

        <p>You can buy the book&nbsp;<a href="http://geni.us/YWSzZ">here</a></p>
        """
    },
    {
     "title": "The Health Benefits of Food",
     "text": """<h2>Dig into the science of why some foods can make you feel better.</h2>

<p><img alt="thumb_1712_content_main" src="http://www.joybauer.com/wp-content/uploads/2016/02/thumb_1712_content_main.jpg" style="height:85px; width:165px" />You know that certain foods can help you lose weight and lower your risk for disease &mdash; but do you know why? Discover your path to better health and nutrition &mdash; read why certain nutrients, vitamins, and minerals naturally found in food can improve your health and help you live a long, active life.</p>

<p><a href="https://joybauer.com/food-articles/oils-and-fats/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2019_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/oils-and-fats/">Oils and Fats</a></h2>

<p>Fat is not a four-letter word! Learn to choose the right fats to add flavor and boost your health.</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/fruit-and-vegetable-juice/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2021_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/fruit-and-vegetable-juice/">Fruit and Vegetable Juice</a></h2>

<p>Fruit juice is a highly concentrated source of fruit sugar. This can raise your blood sugar quickly, and that&rsquo;s why juice is not recommended for people with type 2 diabetes.</p>

<p><a href="https://joybauer.com/food-articles/refined-grains/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2072_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/refined-grains/">Refined Grains</a></h2>

<p>Refined grains are missing fiber and key nutrients that their whole-grain counterparts retain. Don&#39;t miss out on those good-for-you parts &mdash; go for the whole grains instead!</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/starchy-vegetables/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2071_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/starchy-vegetables/">Starchy Vegetables</a></h2>

<p>Starchy vegetables are high-quality carbs that contain valuable nutrients, but they&#39;re more calorie-dense than nonstarchy, water-rich varieties, so be sure to eat them in moderation.</p>

<p><a href="https://joybauer.com/food-articles/coffee-and-tea/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2041_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/coffee-and-tea/">Coffee and Tea</a></h2>

<p>Tea and coffee may wake you up and keep you focused, but don&#39;t overdo it on the caffeine &mdash; it may trigger migraines or IBS in people who are sensitive.</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/condiments/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2004_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/condiments/">Condiments, Sauces, and Flavorings</a></h2>

<p>Not all flavorings are created equal! Before you top your dish with mayo, ketchup, soy sauce, or other condiments, check out how they may affect your health.</p>

<p><a href="https://joybauer.com/food-articles/chocolate/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2044_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/chocolate/">Chocolate</a></h2>

<p>Revel in the potential health benefits of chocolate, but don&#39;t overindulge! Chocolate is still rich in calories, sugar, and fat that can bust your diet if you overdo it.</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/allium-vegetables/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2015_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/allium-vegetables/">Allium Vegetables</a></h2>

<p>They may be best known for their pungent aromas, but these potent veggies, including onions, garlic, and leeks, have powerful effects on your health.</p>

<p><a href="https://joybauer.com/food-articles/cheese/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2037_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/cheese/">Cheese</a></h2>

<p>There are many different cheeses in the world &mdash; and in your supermarket &mdash; but the healthiest choices are cheeses that are lower in fat and sodium.</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/fish-and-shellfish/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2022_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/fish-and-shellfish/">Fish and Shellfish</a></h2>

<p>Fruits of the sea, like fish and shellfish, are some of the best choices of lean protein available &mdash; as long as you don&#39;t fry them or drown them in butter!</p>

<p><a href="https://joybauer.com/food-articles/dairy/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2024_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/dairy/">Dairy</a></h2>

<p>Dairy products are a great source of calcium and protein, but if you&#39;re consuming full-fat dairy you may be increasing your risk of some conditions.</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/cruciferous-vegetables/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2023_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/cruciferous-vegetables/">Cruciferous Vegetables</a></h2>

<p>Cruciferous vegetables like broccoli and brussels sprouts are filling and full of nutrients that help keep you healthy! But if you have IBS, you may want to watch how much of them you eat!</p>

<p><a href="https://joybauer.com/food-articles/berries/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2039_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/berries/">Berries</a></h2>

<p>Berries are high in antioxidants which can help your body fight stress and free radicals.</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/alcohol/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2042_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/alcohol/">Alcohol</a></h2>

<p>Alcohol may have some heart-healthy benefits, but excess drinking can lead to weight gain and put you at greater risk for additional health problems.</p>

<p><a href="https://joybauer.com/food-articles/beef-and-pork/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2046_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/beef-and-pork/">Beef and Pork</a></h2>

<p>Go for lean cuts of meat, and don&#39;t beef up your portions!</p>

<p>&nbsp;</p>

<p><a href="https://joybauer.com/food-articles/beans-and-legumes/"><img alt="" src="https://joybauer.com/wp-content/uploads/2016/02/thumb_2016_content_big_wide-150x150.jpg" style="height:150px; width:150px" /></a></p>

<h2><a href="https://joybauer.com/food-articles/beans-and-legumes/">Beans and Other Healthy Legumes</a></h2>

<p>The old children&#39;s rhyme was right: beans ARE good for your heart. So are lentils and other nutritious legumes, which are great sources of vegetarian protein and high-quality carbohydrates. (The other part of that rhyme was right, too!)</p>
 """
    },
    {
    "title":"place to be visit in india",
    "text":""" <h3>&quot;Tea Gardens, Lakes and Pretty little hill-station&quot;</h3>

<h2>Munnar Tourism</h2>

<p>The idyllic hill station Munnar - famous for its tea estates, exotic lush greenery and craggy peaks, is located in the Western Ghats, in the state of Kerala. It serves as the commercial centre for some of the world&rsquo;s largest tea estates. In addition, Munnar has many protected areas which are home to endemic and highly endangered species like the Nilgiri Thar and the Neelakurinji.</p>

<p>&nbsp;</p>

<p>One of the biggest tea-plantation area of South India, Munnar is one of the most beautiful and popular hill-stations of Kerala. Situated on the banks of three rivers- Madupetti, Nallathanni and Periavaru, Munnar is also blessed with natural view-points apart from the tea-plantations. Munnar is divided into Old Munnar, where the tourist information office is, and Munnar, where the bus station and most guest houses are located. The Eravikulam National Park, Salim Ali Bird Sanctuary and tea plantations are its major attractions.</p>



<p>Free . Works Offline . Share Anywhere</p>

<p>Download Now</p>

<h2>Places to Visit In Munnar</h2>

<p><a href="https://www.holidify.com/places/munnar/atukkad-waterfalls-sightseeing-2887.html"><img alt="Atukkad Waterfalls" src="https://www.holidify.com/images/compressed/thumbnail/4748.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/munnar/atukkad-waterfalls-sightseeing-2887.html">Atukkad Waterfalls</a></p>

<p><a href="https://www.holidify.com/places/munnar/echo-point-munnar-sightseeing-2893.html"><img alt="Echo Point, Munnar" src="https://www.holidify.com/images/cmsuploads/thumbnail/Echo_Point_Munnar-Kerala_20170425130759.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/munnar/echo-point-munnar-sightseeing-2893.html">Echo Point, Munnar</a></p>

<p><a href="https://www.holidify.com/places/munnar/pothamedu-view-point-sightseeing-2906.html"><img alt="Pothamedu View Point" src="https://www.holidify.com/images/cmsuploads/thumbnail/4760_20190422153412.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/munnar/pothamedu-view-point-sightseeing-2906.html">Pothamedu View Point</a></p>

<p><a href="https://www.holidify.com/places/munnar/photo-point-sightseeing-2905.html"><img alt="Photo Point" src="https://www.holidify.com/images/cmsuploads/thumbnail/Tea_Gardens_in_Munnar_Town_20170425133834.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/munnar/photo-point-sightseeing-2905.html">Photo Point</a></p>

<p><a href="https://www.holidify.com/places/munnar/tata-tea-or-kdhp-museum-sightseeing-2909.html"><img alt="Tata Tea or KDHP Museum" src="https://www.holidify.com/images/compressed/thumbnail/2616.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/munnar/tata-tea-or-kdhp-museum-sightseeing-2909.html">Tata Tea or KDHP Museum</a></p>

<p><a href="https://www.holidify.com/places/munnar/eravikulam-national-park-sightseeing-2895.html"><img alt="Eravikulam National Park" src="https://www.holidify.com/images/cmsuploads/thumbnail/E1_20170907143409.PNG" /></a></p>

<p><a href="https://www.holidify.com/places/munnar/eravikulam-national-park-sightseeing-2895.html">Eravikulam National Park</a></p>

<hr />
<p><a href="https://www.holidify.com/places/munnar/sightseeing-and-things-to-do.html"><strong>View All Places To Visit In Munnar &gt;</strong></a></p>

<h2>Munnar Packages</h2>

<p>Compare quotes from upto 3 travel agents for free</p>

<ul>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/6285588846_2c9304f1db_b_20190207123306jpg" />
	<p>Blissful Kerala Munnar, Kumarakom &amp; Kochi</p>

	<p><strong>₹ 11,250</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/Thekkady_Water_Supply_System_20190207170318jpg" />
	<p>Splendid Thekkady &amp; Munnar</p>

	<p><strong>₹ 8,499</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/Blue_Hills_and_Tea_Garden_at_Munnar_Kerala_20190207123736jpg" />
	<p>Kerala Honeymoon Special Munnar, Thekkady &amp; Alleppey</p>

	<p><strong>₹ 14,299</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
</ul>

<hr />
<p><a href="https://www.holidify.com/places/munnar/packages.html" onclick="trackPackageButtonClick(&quot;DestPackagesWidget&quot;)"><strong>View All Packages for Munnar &gt;</strong></a></p>

<h2>Budget for Munnar</h2>

<p>From&nbsp;Bangalore&nbsp;</p>

<ul>
	<li>
	<p>&nbsp;</p>

	<p>&nbsp;</p>

	<p><strong>Backpacker Budget</strong></p>

	<p><strong>₹ 5,589</strong>&nbsp;onwards</p>

	<p>View calculations</p>
	</li>
	<li>
	<p>&nbsp;</p>

	<p>&nbsp;</p>

	<p><strong>Mid Range Budget</strong></p>

	<p><strong>₹ 10,878</strong>&nbsp;onwards</p>

	<p>View calculations</p>
	</li>
	<li>
	<p>&nbsp;</p>

	<p>&nbsp;</p>

	<p><strong>Luxury Budget</strong></p>

	<p><strong>₹ 20,144</strong>&nbsp;onwards</p>

	<p>View calculations</p>
	</li>
</ul>

<p>Includes 2 nights stay, on twin-sharing basis.</p>

<h2>More on Munnar</h2>

<hr />
<h2>Tea Gardens in Munnar</h2>

<hr />
<h2>Restaurants and Local Food in Munnar</h2>

<hr />
<h2>Itinerary</h2>

<hr />
<h2><a href="https://www.holidify.com/places/munnar/best-time-to-visit.html">Best time to Visit Munnar</a></h2>

<hr />
<h2><a href="https://www.holidify.com/places/munnar/how-to-reach.html#commutingWithin">Commuting within Munnar</a></h2>

<h2>Related Posts about Munnar</h2>

<p><a href="https://www.holidify.com/pages/tea-gardens-of-munnar-337.html"><img src="https://www.holidify.com/images/cmsuploads/thumbnail/Munnar66_20171216205538.jpg" />Resplendent Tea Gardens Of Munnar</a></p>

<p><a href="https://www.holidify.com/collections/places-to-visit-near-munnar"><img src="https://www.holidify.com/images/bgImages/MUNNAR.jpg" />Places to visit near Munnar</a></p>

<p><a href="https://www.holidify.com/pages/neelakurinji-munnar-726.html"><img src="https://www.holidify.com/images/cmsuploads/thumbnail/hills-960125_960_720_20180615182442.jpg" />Neelakurinji In Munnar: Heaven Unveils Its Grandeur After 12 Years</a></p>

<p><a href="https://www.holidify.com/blog/must-visit-places-in-south-india/"><img src="https://www.holidify.com/images/small/39.jpg" />Exotic Destinations in Southern India</a></p>

<p><a href="https://www.holidify.com/blog/places-to-visit-in-winter-in-india/"><img src="https://www.holidify.com/images/small/75.jpg" />Best Places for Winters</a></p>

<p><a href="https://www.holidify.com/blog/flowering-delights-in-india/"><img src="https://www.holidify.com/images/small/221.jpg" />Beautiful Flowering Valleys in India</a></p>

<hr />
<p><a href="https://www.holidify.com/places/munnar/related-stories.html"><strong>View All Posts About Munnar &gt;</strong></a></p>

<h2>Rate Munnar</h2>

<p>5 stars4 stars3 stars2 stars1 star</p>

<h4>Munnar Reviews</h4>

<p>3 weeks ago&nbsp;by&nbsp;Yatrika Tours Pvt Ltd&nbsp;</p>

<p>Great post. I was checking continuously this blog and I am impressed! Extremely useful info specially the ultimate part I take care of such information a lot. I was seeking this certain information fo&nbsp;(Read More)</p>

<p>7 months ago&nbsp;by&nbsp;Couponsji India&nbsp;</p>

<p>Munnar is truly the home of the God, the all-encompassing verdant scenario might have enticed the lord to such extent that he decided to make the place his abode. From Munnar to Alleppey every bit of&nbsp;(Read More)</p>

<p>7 months ago&nbsp;by&nbsp;Rohit Shroff&nbsp;</p>

<p>- Apply sunscreen lotion while you leave Munnar because as you descend the hills the weather gets warmer and causes sun burn. Hill stations tend to get dark rather early, so be sure to carry a torch o&nbsp;(Read More)</p>

<p>7 months ago&nbsp;by&nbsp;Rohit Shroff&nbsp;</p>

<p>Day 1 &ndash;Have breakfast and begin your trip early in the morning with Pothamedu View Point adorned with stretching hills and lush green mountains. Chithirapuram is the next destination on the list follo&nbsp;(Read More)</p>

<p>7 months ago&nbsp;by&nbsp;Taniya Batra&nbsp;</p>

<p>Munnar is a beautiful hill station that is ideal for escaping the sweltering heat of the cities. Known best for its tea estates Munnar has a lot of sights to behold and is enjoyable throughout the yea&nbsp;(Read More)</p>

<hr />
<p><strong>View All Reviews &gt;</strong></p>

<hr />
<h5>Add a Review</h5>

<p>5 stars4 stars3 stars2 stars1 star</p>

<p>Write your Review</p>

<h2>Munnar Photos</h2>

<p><img src="https://www.holidify.com/res/images/patt.png" title="Munnar is a beautiful town in Kerala State at an elevation of 1,532 m" /><img src="https://www.holidify.com/res/images/patt.png" title="Located in the Idukki district, Munnar is also called as Kashmir of South India" /><img src="https://www.holidify.com/res/images/patt.png" title="Munnar is surrounded by rolling hills dotted with tea plantations established in the late 19th century." /></p>

<p><img src="https://www.holidify.com/res/images/patt.png" title="#" /></p>

<p>+ 57<br />
photos</p>

<hr />
<p><a href="https://www.holidify.com/places/munnar/photos.html"><strong>All Photos of Munnar &gt;&gt;</strong></a></p>

<h2><img src="https://www.holidify.com/res/images/patt.png" style="height:30px" />&nbsp;Holidify&#39;s Opinion</h2>

<h2>&nbsp; What&#39;s Great?</h2>

<p>A new hub for the honeymooners. Extremely peaceful place. The pleasant weather is always a delight for the tourists.</p>

<h2>&nbsp; What&#39;s not so Great?</h2>

<p>Public transport for commuting in the local areas is a bit problematic. Also, Munnar does not have its own railway station and airport which makes it difficult to access.</p>

<h2>For Whom</h2>

<p>A very romantic place for the couples and honeymooners. Also, a favourable destination for the nature lovers and trekkers.</p>

<h2>Hotels in Munnar</h2>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Search</p>

<h2>Top Hotels in Munnar</h2>

<ul>
	<li><img src="https://www.holidify.com/res/images/patt.png" />
	<p>The Shade</p>

	<p><strong>INR 3,000</strong>&nbsp;/night onwards</p>
	</li>
	<li><img src="https://www.holidify.com/res/images/patt.png" />
	<p>Chandys Windy Woods</p>

	<p><strong>INR 7,485</strong>&nbsp;/night onwards</p>
	</li>
	<li><img src="https://www.holidify.com/res/images/patt.png" />
	<p>The Panoramic Getaway</p>

	<p><strong>INR 7,450</strong>&nbsp;/night onwards</p>
	</li>
</ul>

<hr />
<p><a href="https://www.holidify.com/places/munnar/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;InContent_ViewAllHotels&quot;)"><strong>View All Hotels in Munnar &gt;</strong></a></p>

<p>Ad</p>

<h2>How to Reach Munnar</h2>

<p>Kochi at 130 km is the nearest airport. Angamaly is the closest railhead 120 km away, with Kochi station as the next alternative. Regular buses and tourist taxis connect Kochi to Munnar.&nbsp;<a href="https://www.holidify.com/places/munnar/how-to-reach.html">(Read More)</a></p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/chennai-to-munnar-1208.html">From Chennai&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/chennai-to-munnar-1208.html">584 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/chennai-to-munnar-1208.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/munnar/how-to-reach/bangalore-to-munnar-1210.html">From Bangalore&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/bangalore-to-munnar-1210.html">476 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/bangalore-to-munnar-1210.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/munnar/how-to-reach/ernakulam-to-munnar-1203.html">From Ernakulam&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/ernakulam-to-munnar-1203.html">129 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/ernakulam-to-munnar-1203.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/munnar/how-to-reach/alleppey-to-munnar-1204.html">From Alleppey&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/alleppey-to-munnar-1204.html">176 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/alleppey-to-munnar-1204.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/munnar/how-to-reach/hyderabad-to-munnar-1202.html">From Hyderabad&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/hyderabad-to-munnar-1202.html">1,044 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/hyderabad-to-munnar-1202.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/munnar/how-to-reach/delhi-to-munnar-1209.html">From Delhi&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/delhi-to-munnar-1209.html">2,641 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/munnar/how-to-reach/delhi-to-munnar-1209.html">View Details</a></p>

<h4>Latest questions by travellers on Munnar</h4>

<p>What is the best time to visit Munnar and how many days are required to explore?</p>

<p><img src="https://www.holidify.com/res/images/first_to_answer.png" />&nbsp;Be the first to add an answer</p>

<hr />
<p><strong>View All Questions about Munnar &gt;</strong></p>

<hr />
<p>Ask a question from people who travelled to Munnar recently</p>

<p><img src="https://www.holidify.com/res/images/patt.png" /></p>

<p>Shreyas and 223 others have others have helped over 1,000 users travelling to Munnar</p>

<p>Submit Question</p>

<h3>Nearby Places</h3>

<p><a href="https://www.holidify.com/places/kodaikanal/" title="Kodaikanal"><img src="https://www.holidify.com/images/tooltipImagesSmall/KODAIKANAL.jpg" /><br />
Kodaikanal&nbsp;</a><br />
<a href="https://www.holidify.com/places/kodaikanal/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/ooty/" title="Ooty"><img src="https://www.holidify.com/images/tooltipImagesSmall/OOTY.jpg" /><br />
Ooty&nbsp;</a><br />
<a href="https://www.holidify.com/places/ooty/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/thekkady/" title="Thekkady"><img src="https://www.holidify.com/images/tooltipImagesSmall/THEKKADY.jpg" /><br />
Thekkady&nbsp;</a><br />
<a href="https://www.holidify.com/places/thekkady/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/alleppey/" title="Alleppey"><img src="https://www.holidify.com/images/tooltipImagesSmall/ALLEPPEY.jpg" /><br />
Alleppey&nbsp;</a><br />
<a href="https://www.holidify.com/places/alleppey/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/thattekad-bird-sanctuary/" title="Thattekad Bird Sanctuary"><img src="https://www.holidify.com/images/tooltipImagesSmall/THATTEKAD-BIRD-SANCTUARY.jpg" /><br />
Thattekad Bird Sanctuary&nbsp;</a><br />
<a href="https://www.holidify.com/places/thattekad-bird-sanctuary/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/devikulam/" title="Devikulam"><img src="https://www.holidify.com/images/tooltipImagesSmall/DEVIKULAM.jpg" /><br />
Devikulam&nbsp;</a><br />
<a href="https://www.holidify.com/places/devikulam/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p>Ad</p>

<h3>Similar Places</h3>

<p><a href="https://www.holidify.com/places/ooty/" title="Ooty"><img src="https://www.holidify.com/images/tooltipImagesSmall/OOTY.jpg" /><br />
Ooty&nbsp;</a><br />
<a href="https://www.holidify.com/places/ooty/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/auli/" title="Auli"><img src="https://www.holidify.com/images/tooltipImagesSmall/AULI.jpg" /><br />
Auli&nbsp;</a><br />
<a href="https://www.holidify.com/places/auli/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/kodaikanal/" title="Kodaikanal"><img src="https://www.holidify.com/images/tooltipImagesSmall/KODAIKANAL.jpg" /><br />
Kodaikanal&nbsp;</a><br />
<a href="https://www.holidify.com/places/kodaikanal/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/gangtok/" title="Gangtok"><img src="https://www.holidify.com/images/tooltipImagesSmall/GANGTOK.jpg" /><br />
Gangtok&nbsp;</a><br />
<a href="https://www.holidify.com/places/gangtok/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p>Ad</p>
"""
    },
    {
    "title":"places to be visit in india(GOA) ",
    "text": """ <h3>&quot;Beaches, Sunsets and Crazy Nights&quot;</h3>

<h2>Goa Tourism</h2>

<p>Lying on the west coast, Goa is one of the smallest states in India known for its brilliant beaches, scrumptious food and Portuguese heritage. Panjim, the capital city located in the centre is well-connected with an international airport and roads and trains run from North to South part of Goa.</p>

<p>&nbsp;</p>

<p>With a coastline stretching for over 100 kilometres, Goa has numerous beaches that attract millions of visitors. While Baga and Calangute are more popular among the Indian family crowd, Anjuna and Arambol draw a lot of foreign tourists. The beaches in South Goa are relatively lesser explored, but some of them like Agonda and Palolem are more beautiful.&nbsp;<br />
<br />
A former Portuguese colony, Goa also boasts of beautiful architecture from the colonial era with many churches and old-style bungalows. The people are quite friendly towards tourists and celebrate many festivals throughout the year. While the seafood is excellent, Goa has one of the best nightlife in the country with trendy bars, beach shacks, elegant cafes and many clubs and discotheques. Thanks to lower alcohol prices in the state, Goa is also great for younger tourists with relatively tighter pockets.</p>

<p><strong>Download Goa PDF Guide</strong></p>

<p>Free . Works Offline . Share Anywhere</p>

<p>Download Now</p>

<h2>Places to Visit In Goa</h2>

<p><a href="https://www.holidify.com/places/goa/calangute-beach-sightseeing-6227.html"><img alt="Calangute Beach" src="https://www.holidify.com/images/cmsuploads/thumbnail/attr_wiki_1173_20190502124122.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/goa/calangute-beach-sightseeing-6227.html">Calangute Beach</a></p>

<p><a href="https://www.holidify.com/places/goa/baga-beach-sightseeing-6226.html"><img alt="Baga Beach" src="https://www.holidify.com/images/compressed/thumbnail/7691.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/goa/baga-beach-sightseeing-6226.html">Baga Beach</a></p>

<p><a href="https://www.holidify.com/places/goa/basilica-of-bom-jesus-sightseeing-1840.html"><img alt="Basilica of Bom Jesus" src="https://www.holidify.com/images/cmsuploads/thumbnail/attr_1840.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/goa/basilica-of-bom-jesus-sightseeing-1840.html">Basilica of Bom Jesus</a></p>

<p><a href="https://www.holidify.com/places/goa/anjuna-beach-sightseeing-1837.html"><img alt="Anjuna Beach" src="https://www.holidify.com/images/cmsuploads/thumbnail/A2_20170923154029.PNG" /></a></p>

<p><a href="https://www.holidify.com/places/goa/anjuna-beach-sightseeing-1837.html">Anjuna Beach</a></p>

<p><a href="https://www.holidify.com/places/goa/arambol-beach-sightseeing-1838.html"><img alt="Arambol Beach" src="https://www.holidify.com/images/compressed/thumbnail/3201.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/goa/arambol-beach-sightseeing-1838.html">Arambol Beach</a></p>

<p><a href="https://www.holidify.com/places/goa/flea-markets-sightseeing-1855.html"><img alt="Flea Markets" src="https://www.holidify.com/images/cmsuploads/thumbnail/landscape-tree-nature-forest-grass-plant-1455627-pxhere.com_20190412091036.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/goa/flea-markets-sightseeing-1855.html">Flea Markets</a></p>

<hr />
<p><a href="https://www.holidify.com/places/goa/sightseeing-and-things-to-do.html"><strong>View All Places To Visit In Goa &gt;</strong></a></p>

<h2>Goa Packages</h2>

<p>Compare quotes from upto 3 travel agents for free</p>

<ul>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/Fort_aguada_20190206173930jpg" />
	<p>Goa Sightseeing Tour</p>

	<p><strong>₹ 9,999</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/3194_20190206175122jpg" />
	<p>Budget Trip Goa</p>

	<p><strong>₹ 12,000</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/3195_20190206190648jpg" />
	<p>Mesmerizing Goa - Beaches and Sightseeing</p>

	<p><strong>₹ 15,000</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
</ul>

<hr />
<p><a href="https://www.holidify.com/places/goa/packages.html" onclick="trackPackageButtonClick(&quot;DestPackagesWidget&quot;)"><strong>View All Packages for Goa &gt;</strong></a></p>

<h2>More on Goa</h2>

<hr />
<h2>North and South Goa</h2>

<hr />
<h2>What Makes Goa An Amazing Tourist Destination</h2>

<hr />
<h2>Nightlife of Goa</h2>

<hr />
<h2>Best Time for Adventure Seekers</h2>

<hr />
<h2>Best Time for Honeymooners</h2>

<hr />
<h2>Tips</h2>

<hr />
<h2>Beaches of Goa</h2>

<hr />
<h2>History of Goa</h2>

<hr />
<h2>Culture of Goa</h2>

<hr />
<h2>Budget</h2>

<hr />
<h2>Restaurants and Local Food in Goa</h2>

<hr />
<h2>Itinerary</h2>

<hr />
<h2><a href="https://www.holidify.com/places/goa/best-time-to-visit.html">Best time to Visit Goa</a></h2>

<hr />
<h2><a href="https://www.holidify.com/places/goa/how-to-reach.html#commutingWithin">Commuting within Goa</a></h2>

<h2>Related Posts about Goa</h2>

<p><a href="https://www.holidify.com/blog/best-beaches-in-goa/"><img src="https://www.holidify.com/images/small/19.jpg" />Best Beaches in Goa</a></p>

<p><a href="https://www.holidify.com/blog/things-not-to-do-in-goa/"><img src="https://www.holidify.com/images/small/181.jpg" />Things NOT to do in Goa</a></p>

<p><a href="https://www.holidify.com/pages/nightlife-in-goa-things-to-do-1334.html"><img src="https://www.holidify.com/blog/wp-content/uploads/2014/10/saturday-night-market.jpg" />Nightlife in Goa - Parties and Nightclubs in Goa</a></p>

<p><a href="https://www.holidify.com/pages/what-to-wear-in-goa-263.html"><img src="https://www.holidify.com/images/cmsuploads/thumbnail/4851668770_4a97c3c342_b_20170920114728.jpg" />Holiday Look-book: A Complete Guide To Your Wardrobe When In Goa</a></p>

<p><a href="https://www.holidify.com/collections/places-to-visit-near-goa"><img src="https://www.holidify.com/images/bgImages/GOA.jpg" />Places to visit near Goa</a></p>

<p><a href="https://www.holidify.com/pages/nightlife-in-south-goa-433.html"><img src="https://www.holidify.com/images/cmsuploads/thumbnail/Liquid-Sky_20180402121937.jpg" />Nightlife In South Goa - 15 Places To Groove To Your Madness</a></p>

<hr />
<p><a href="https://www.holidify.com/places/goa/related-stories.html"><strong>View All Posts About Goa &gt;</strong></a></p>

<h2>Rate Goa</h2>

<p>5 stars4 stars3 stars2 stars1 star</p>

<h4>Goa Reviews</h4>

<p>1 week ago&nbsp;by&nbsp;Ken Chiramel&nbsp;</p>

<p>The holiday destination favourite of many Indians and foreigners alike, Goa offers something for every traveller. The beaches of Baga and Anjuna give tourists the beaches teeming with families and wat&nbsp;(Read More)</p>

<p>1 month ago&nbsp;by&nbsp;Arun Kumar&nbsp;</p>

<p>goa is a biggest tourist attraction in India and the world. Goa is a tourist capital in india. top 10 tourist place in india</p>

<p>7 months ago&nbsp;by&nbsp;Yash Saboo&nbsp;</p>

<p>Goa Beyond Beaches There&rsquo;s something about Goa which drags me back to it almost every year. The beaches, pristine blue with golden sand is a sight I can imagine with my eyes closed. But there&rsquo;s so muc&nbsp;(Read More)</p>

<p>7 months ago&nbsp;by&nbsp;Kovid Kapoor&nbsp;</p>

<p>- Don&#39;t forget to carry beachwear, sunscreen, hat, a pair of flip-flops, and sunglasses.- If you&#39;re planning a trip between June-September, don&#39;t forget to carry your rain gear. The Rain gods have qui&nbsp;(Read More)</p>

<p>7 months ago&nbsp;by&nbsp;Ishita Solanki&nbsp;</p>

<p>We went to Goa by train from Manipal. The weather was amazing throughout the trip. We first went to Fort Aguada, which was some ruins on the edge of the cliff with a majestic view of the sea. Next was&nbsp;(Read More)</p>

<hr />
<p><strong>View All Reviews &gt;</strong></p>

<hr />
<h5>Add a Review</h5>

<p>5 stars4 stars3 stars2 stars1 star</p>

<p>Write your Review</p>

<h2>Goa Photos</h2>

<p><img src="https://www.holidify.com/images/cmsuploads/thumbnail/Optimized-top_gear_pub-638x405_20190412164306.jpg" title="Top Gear Pub in Goa" /><img src="https://www.holidify.com/images/cmsuploads/thumbnail/Anjuna_goa_shacks_20190412165511.JPG" title="" /><img src="https://www.holidify.com/images/cmsuploads/thumbnail/Anjuna_beach_Goa_20190412165717.jpg" title="" /></p>

<p><img src="https://www.holidify.com/images/bgImages/GOA.jpg" title="#" /></p>

<p>+ 288<br />
photos</p>

<hr />
<p><a href="https://www.holidify.com/places/goa/photos.html"><strong>All Photos of Goa &gt;&gt;</strong></a></p>

<h2><img src="https://www.holidify.com/res/images/holidify_logo_opinion.png" style="height:30px" />&nbsp;Holidify&#39;s Opinion</h2>

<h2>&nbsp; What&#39;s Great?</h2>

<p>Beautiful beaches and scenery. Get a first hand taste of Portuguese culture and architecture. Amazing nightlife. Frequent music concerts.</p>

<p>&nbsp;</p>

<h2>&nbsp; What&#39;s not so Great?</h2>

<p>In the peak seasons, Goa can be very crowded. Can be expensive. Summers could be extreme.</p>

<h2>For Whom</h2>

<p>The Party Capital of India, Goa is for anyone who wishes to take a break from their routine life and relax by the beach. From youngsters, spinsters, bachelors, honeymooners to working adults - everyone gets their share of fun at Goa.</p>

<h2>Hotels in Goa</h2>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Search</p>

<h2>Top Hotels in Goa</h2>

<ul>
	<li><img src="https://q-xx.bstatic.com/xdata/images/hotel/max300/131833415.jpg?k=975ad1d8d07d7d7cb459cce32c0440cc3b77cf1ff9cee4774bf3990b07d7f319&amp;o=" />
	<p>Resort Coqueiral</p>

	<p><strong>INR 4,661</strong>&nbsp;/night onwards</p>
	</li>
	<li><img src="https://q-xx.bstatic.com/xdata/images/hotel/max300/139451887.jpg?k=0d329745bf072817edd09d0e5da9d2e1eb616f6a36db00b1228769c840ea66f1&amp;o=" />
	<p>Lemonmint Svelton Manor</p>

	<p><strong>INR 1,999</strong>&nbsp;/night onwards</p>
	</li>
	<li><img src="https://q-xx.bstatic.com/xdata/images/hotel/max300/60029006.jpg?k=ab74aba82f84d2f2d0f1f853823e43e6c2f8005d33b76a81b8fa3098e48fa42a&amp;o=" />
	<p>Vivanta Panaji, Goa</p>

	<p><strong>INR 5,400</strong>&nbsp;/night onwards</p>
	</li>
</ul>

<hr />
<p><a href="https://www.holidify.com/places/goa/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;InContent_ViewAllHotels&quot;)"><strong>View All Hotels in Goa &gt;</strong></a></p>

<p>Ad</p>

<h2>Neighbourhoods in Goa</h2>

<p><a href="https://www.holidify.com/places/goa/madgaon-places-to-visit-area.html"><img src="https://www.holidify.com/res/images/patt.png" /></a></p>

<p><a href="https://www.holidify.com/places/goa/madgaon-places-to-visit-area.html">Madgaon</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/panaji-places-to-visit-area.html"><img src="https://www.holidify.com/res/images/patt.png" /></a></p>

<p><a href="https://www.holidify.com/places/goa/panaji-places-to-visit-area.html">Panaji</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/north-goa-places-to-visit-area.html"><img src="https://www.holidify.com/res/images/patt.png" /></a></p>

<p><a href="https://www.holidify.com/places/goa/north-goa-places-to-visit-area.html">North Goa</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/south-goa-places-to-visit-area.html"><img src="https://www.holidify.com/res/images/patt.png" /></a></p>

<p><a href="https://www.holidify.com/places/goa/south-goa-places-to-visit-area.html">South Goa</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/vasco-da-gama-places-to-visit-area.html"><img src="https://www.holidify.com/res/images/patt.png" /></a></p>

<p><a href="https://www.holidify.com/places/goa/vasco-da-gama-places-to-visit-area.html">Vasco Da Gama</a></p>

<h2>How to Reach Goa</h2>

<p>With over 2 million tourists coming in every year, Goa has to be well connected and accessible. Goa is easily accessible by road, rail and air. Being such a popular holiday destination, there are v...<a href="https://www.holidify.com/places/goa/how-to-reach.html">(Read More)</a></p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/bangalore-to-goa-539.html">From Bangalore&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/bangalore-to-goa-539.html">557 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/bangalore-to-goa-539.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/how-to-reach/mumbai-to-goa-547.html">From Mumbai&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/mumbai-to-goa-547.html">583 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/mumbai-to-goa-547.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/how-to-reach/hyderabad-to-goa-520.html">From Hyderabad&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/hyderabad-to-goa-520.html">637 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/hyderabad-to-goa-520.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/how-to-reach/delhi-to-goa-537.html">From Delhi&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/delhi-to-goa-537.html">1,876 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/delhi-to-goa-537.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/how-to-reach/chennai-to-goa-534.html">From Chennai&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/chennai-to-goa-534.html">910 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/chennai-to-goa-534.html">View Details</a></p>

<p>&nbsp;<a href="https://www.holidify.com/places/goa/how-to-reach/ahmedabad-to-goa-541.html">From Ahmedabad&nbsp;</a></p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/ahmedabad-to-goa-541.html">1,096 km</a></p>

<p>&nbsp;</p>

<p><a href="https://www.holidify.com/places/goa/how-to-reach/ahmedabad-to-goa-541.html">View Details</a></p>

<h4>Latest questions by travellers on Goa</h4>

<p>Amreli to Goa distance?</p>

<p><img src="https://www.holidify.com/res/images/first_to_answer.png" />&nbsp;Be the first to add an answer</p>

<hr />
<p><strong>View All Questions about Goa &gt;</strong></p>

<hr />
<p>Ask a question from people who travelled to Goa recently</p>

<p><img src="https://www.holidify.com/res/images/patt.png" /></p>

<p>Shreyas and 223 others have others have helped over 1,000 users travelling to Goa</p>

<p>Submit Question</p>

<h3>Nearby Places</h3>

<p><a href="https://www.holidify.com/places/tarkarli/" title="Tarkarli"><img src="https://www.holidify.com/images/tooltipImagesSmall/TARKARLI.jpg" /><br />
Tarkarli&nbsp;</a><br />
<a href="https://www.holidify.com/places/tarkarli/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/gokarna/" title="Gokarna"><img src="https://www.holidify.com/images/tooltipImagesSmall/GOKARNA.jpg" /><br />
Gokarna&nbsp;</a><br />
<a href="https://www.holidify.com/places/gokarna/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/malvan/" title="Malvan"><img src="https://www.holidify.com/images/tooltipImagesSmall/MALVAN.jpg" /><br />
Malvan&nbsp;</a><br />
<a href="https://www.holidify.com/places/malvan/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/amboli/" title="Amboli"><img src="https://www.holidify.com/images/tooltipImagesSmall/AMBOLI.jpg" /><br />
Amboli&nbsp;</a><br />
<a href="https://www.holidify.com/places/amboli/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/devbagh/" title="Devbagh"><img src="https://www.holidify.com/images/tooltipImagesSmall/DEVBAGH.jpg" /><br />
Devbagh&nbsp;</a><br />
<a href="https://www.holidify.com/places/devbagh/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/hampi/" title="Hampi"><img src="https://www.holidify.com/images/tooltipImagesSmall/HAMPI.jpg" /><br />
Hampi&nbsp;</a><br />
<a href="https://www.holidify.com/places/hampi/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p>Ad</p>

<p>&nbsp;</p>

<h3>Similar Places</h3>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/" title="Andaman &amp; Nicobar Islands"><img src="https://www.holidify.com/images/tooltipImagesSmall/ANDAMAN-NICOBAR-ISLANDS.jpg" /><br />
Andaman &amp; Nicobar Islands&nbsp;</a><br />
<a href="https://www.holidify.com/places/andaman-nicobar-islands/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/gokarna/" title="Gokarna"><img src="https://www.holidify.com/images/tooltipImagesSmall/GOKARNA.jpg" /><br />
Gokarna&nbsp;</a><br />
<a href="https://www.holidify.com/places/gokarna/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/pondicherry/" title="Pondicherry"><img src="https://www.holidify.com/images/tooltipImagesSmall/PONDICHERRY.jpg" /><br />
Pondicherry&nbsp;</a><br />
<a href="https://www.holidify.com/places/pondicherry/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p><a href="https://www.holidify.com/places/varkala/" title="Varkala"><img src="https://www.holidify.com/images/tooltipImagesSmall/VARKALA.jpg" /><br />
Varkala&nbsp;</a><br />
<a href="https://www.holidify.com/places/varkala/sightseeing-and-things-to-do.html">Places To Visit</a></p>

<p>Ad</p>
"""
    },
    {
    "title":"places to visit in india(AGRA)",
    "text":"""<ul>
	<li><a href="https://www.holidify.com/places/agra/" title="Agra Tourism">Overview</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/agra/sightseeing-and-things-to-do.html" title="Places to visit in Agra">Places to Visit&nbsp;</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/agra/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;DestSecondaryHeader&quot;)" title="Hotels in Agra">Hotels</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/agra/how-to-reach.html" title="How to reach Agra">How to Reach</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/agra/best-time-to-visit.html" title="Best time to visit Agra">Best Time To Visit</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/agra/map-view.html" title="Agra Tourist Map">Map</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/agra/photos.html" title="Photos of Agra">Photos</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/agra/restaurants-places-to-eat-local-cuisine.html" title="Restaurants in Agra">Food</a></li>
</ul>

<p>&nbsp;</p>

<p><img alt="agra photos" src="https://www.holidify.com/images/compressed/thumbnail/3660.jpg?v=1.1" title="Taj Mahal" />&nbsp;<img alt="agra photos" src="https://www.holidify.com/images/compressed/thumbnail/3661.jpg?v=1.1" title="Fatehpur Sikri" />&nbsp;<img src="https://www.holidify.com/images/bgImages/AGRA.jpg" /></p>

<p>View 145<br />
photos</p>

<p><a href="https://www.holidify.com/places/agra/#" id="wishlistButton" onclick="toggleWishlist('DESTINATION');return false;">&nbsp;Wishlist</a></p>

<p>&nbsp;</p>

<h1>Agra</h1>

<p><strong>4.2</strong>&nbsp;/ 5352 votes</p>

<p>&nbsp;<a href="https://www.holidify.com/state/uttar-pradesh/">Uttar Pradesh&nbsp;</a>|&nbsp;<a href="https://www.holidify.com/country/india/">India</a></p>

<p>&nbsp;State rank:&nbsp;2 out of 14&nbsp;<a href="https://www.holidify.com/state/uttar-pradesh/top-destinations-places-to-visit.html">Places To Visit In Uttar Pradesh</a></p>

<p>&nbsp;</p>

<p><strong>276</strong>&nbsp;Hotels Found&nbsp;<a href="https://www.holidify.com/places/agra/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;DestATFViewHotel&quot;)">(View All)</a></p>

<p><a href="https://www.holidify.com/places/agra/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;DestATFButton&quot;)">View Hotels in Agra</a></p>

<hr />
<p>&nbsp;Weather:&nbsp;<img src="https://www.holidify.com/images/logos/weather-icons/partly-cloudy-day" />&nbsp;39&deg; C</p>

<p>&nbsp;Ideal duration:&nbsp;1-2 days</p>

<p>&nbsp;Best time:&nbsp;Oct-Mar&nbsp;(Read More)</p>

<p>&nbsp;Nearest Airport:&nbsp;Agra&nbsp;(Check Flights)</p>

<p>Ad</p>

<p>&nbsp;</p>

<h3>&quot;The city of Taj Mahal, the monument of eternal love&quot;</h3>

<h2>Agra Tourism</h2>

<p>Home to one of the 7 wonders of the world, the&nbsp;<a href="https://www.holidify.com/places/agra/taj-mahal-sightseeing-1020.html">Taj Mahal</a>, Agra is a sneak peek into the architectural history with other structures such as&nbsp;<a href="https://www.holidify.com/places/agra/agra-fort-sightseeing-1013.html">Agra Fort</a>&nbsp;and&nbsp;<a href="https://www.holidify.com/places/agra/fatehpur-sikri-sightseeing-1015.html">Fatehpur Sikri</a>&nbsp;and hence makes for a must visit for anyone living in or visiting India.</p>

<p>&nbsp;</p>

<p>When you talk about Agra, one thing has to stand out - yes, the Taj Mahal. Agra is host to the only one of the Seven Wonders of the World in India, Taj Mahal, which makes the whole country proud. But that&#39;s not the only thing Agra has to boast of. Agra has three UNESCO World Heritage sites and Taj Mahal features in the 50 most popular tourist destinations in the world. History, architecture, romance all together create the magic of Agra which is almost the lifeline of Indian tourism. History fanatics as well as architecture buffs can have a ball here with the sheer expanse of the Mughal art and culture on display. Apart from its monuments, the city also has some exciting stuff for foodies - including the famous Agra ka Petha and amazing chaat and Lassi.</p>

<p><a href="https://www.holidify.com/places/agra/">READ MORE</a><strong>Download Agra PDF Guide</strong></p>

<p>Free . Works Offline . Share Anywhere</p>

<p>Download Now</p>

<h2>Places to Visit In Agra</h2>

<p><a href="https://www.holidify.com/places/agra/taj-mahal-sightseeing-1020.html"><img alt="Taj Mahal" src="https://www.holidify.com/images/cmsuploads/thumbnail/attr_1448_20190212100722jpg" /></a></p>

<p><a href="https://www.holidify.com/places/agra/taj-mahal-sightseeing-1020.html">Taj Mahal</a></p>

<p><a href="https://www.holidify.com/places/agra/fatehpur-sikri-sightseeing-1015.html"><img alt="Fatehpur Sikri" src="https://www.holidify.com/images/compressed/thumbnail/3661.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/agra/fatehpur-sikri-sightseeing-1015.html">Fatehpur Sikri</a></p>

<p><a href="https://www.holidify.com/places/agra/agra-fort-sightseeing-1013.html"><img alt="Agra Fort" src="https://www.holidify.com/images/cmsuploads/thumbnail/attr_1013.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/agra/agra-fort-sightseeing-1013.html">Agra Fort</a></p>

<p><a href="https://www.holidify.com/places/agra/itimad-ud-daulahs-tomb-sightseeing-1016.html"><img alt="Itimad-ud-daulah's Tomb" src="https://www.holidify.com/images/cmsuploads/thumbnail/3663_20190503221321.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/agra/itimad-ud-daulahs-tomb-sightseeing-1016.html">Itimad-ud-daulah&#39;s Tomb</a></p>

<p><a href="https://www.holidify.com/places/agra/shopping-in-agra-sightseeing-1014.html"><img alt="Shopping in Agra" src="https://www.holidify.com/images/cmsuploads/thumbnail/4037_20190504135116.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/agra/shopping-in-agra-sightseeing-1014.html">Shopping in Agra</a></p>

<p><a href="https://www.holidify.com/places/agra/tomb-of-akbar-sightseeing-1019.html"><img alt="Tomb of Akbar" src="https://www.holidify.com/images/cmsuploads/thumbnail/akbar-tomb-agra-head-255_20171215172135.jpeg" /></a></p>

<p><a href="https://www.holidify.com/places/agra/tomb-of-akbar-sightseeing-1019.html">Tomb of Akbar</a></p>

<hr />
<p><a href="https://www.holidify.com/places/agra/sightseeing-and-things-to-do.html"><strong>View All Places To Visit In Agra &gt;</strong></a></p>

<h2>Hotels in Agra</h2>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Search</p>

<h2>Top Hotels in Agra</h2>

<ul>
	<li><img src="https://q-xx.bstatic.com/xdata/images/hotel/max300/47406117.jpg?k=f01ab160faca14c23beee1c263f4f0c7a3adff125bdab36ae8c542718f694464&amp;o=" />
	<p>The Oberoi Amarvilas Agra</p>

	<p><strong>INR 19,333</strong>&nbsp;/night onwards</p>
	</li>
	<li><img src="https://q-xx.bstatic.com/xdata/images/hotel/max300/31549645.jpg?k=77936d4081dfb6675c270aa56c7f602edbdcceb766a85c3eed96a1a0c66ef0fa&amp;o=" />
	<p>Trident Agra</p>

	<p><strong>INR 3,000</strong>&nbsp;/night onwards</p>
	</li>
	<li><img src="https://q-xx.bstatic.com/xdata/images/hotel/max300/132330227.jpg?k=670290dceba5213d0cdf02a0293c1bdff700719c25c1ebf238df702bcde90675&amp;o=" />
	<p>Max Guest House</p>

	<p><strong>INR 720</strong>&nbsp;/night onwards</p>
	</li>
</ul>

<hr />
<p><a href="https://www.holidify.com/places/agra/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;InContent_ViewAllHotels&quot;)"><strong>View All Hotels in Agra &gt;</strong></a></p>

<h2>More on Agra</h2>

<hr />
<h2>History of Agra</h2>

<hr />
<h2>A confluence of history, culture, and beauty&nbsp;</h2>

<hr />
<h2>Restaurants and Local Food in Agra</h2>

<hr />
<h2>Itinerary</h2>

<hr />
<h2><a href="https://www.holidify.com/places/agra/best-time-to-visit.html">Best time to Visit Agra</a></h2>

<hr />
<h2><a href="https://www.holidify.com/places/agra/how-to-reach.html#commutingWithin">Commuting within Agra</a></h2>

<h2>Related Posts about Agra</h2>
 """
    },
    {
    "title":"place to visit in india(andman island)",
    "text":"""<h3>&quot;Blue seas, virgin islands and colonial past&quot;</h3>

<h2>Andaman &amp; Nicobar Islands Tourism</h2>

<p>Replete with picturesque shimmering beaches, lagoons of turquoise blue waters and a bit of history, Andaman &amp; Nicobar Islands is a little slice of paradise tucked around 1,400 km away from the east coast of India. The union territory comprises a total of 572 islands, only 37 of which are inhabited and a few are open to the tourists.&nbsp;<br />
<br />
Port Blair, the capital city of Andaman &amp; Nicobar Islands, is the gateway to the archipelago and is connected with various islands via multiple daily ferries. Havelock and Neil Island are some of the most famous islands among tourists and is known for pearly white sands, palm-lined shores and offer some of the best snorkelling and diving options in India.</p>

<p>&nbsp;</p>

<p>Once known for its Cellular Jail- &lsquo;Kaala Paani&rsquo; in Port Blair which primarily imprisoned the freedom fighters who were exiled from the mainland of India during the British Era, the graph of the Andaman and Nicobar islands have lately changed drastically and it is now known for its flourishing tourism industry which especially attracts honeymooners, families and adventure enthusiasts.&nbsp;<br />
<br />
You can either laze around on the sandy shores and enjoy the mesmerising sunsets or try your hand at scuba diving and explore the vibrant coral reefs. Besides, it also has virgin immaculate backwaters for those seeking solitude and ataraxy.<br />
<br />
Havelock Island is one of the largest and the most popular attraction of all of Andaman &amp; Nicobar Islands. Blessed with pristine beaches and coconut groves, this one offers myriad adventure sports opportunities to its guests. From snorkelling to parasailing, scuba diving and kayaking etc., there is no dearth of thrilling activities here, for that much-needed adrenaline rush, on an otherwise tranquil leisure vacay.&nbsp;<br />
<br />
In addition to this, you can visit the bustling city of Port Blair to get a glimpse of the local lifestyle. Steeped in colonial history and boasting of striking architectural monuments, you can also browse the local markets and savour the traditional cuisine.</p>

<p><strong>Download Andaman &amp; Nicobar Islands PDF Guide</strong></p>

<p>Free . Works Offline . Share Anywhere</p>

<p>Download Now</p>

<h2>Places to Visit In Andaman &amp; Nicobar Islands</h2>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/scuba-diving-in-andaman-sightseeing-1194.html"><img alt="Scuba Diving In Andaman" src="https://www.holidify.com/images/compressed/thumbnail/4099.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/scuba-diving-in-andaman-sightseeing-1194.html">Scuba Diving In Andaman</a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/havelock-island-sightseeing-1188.html"><img alt="Havelock Island" src="https://www.holidify.com/images/cmsuploads/thumbnail/3617_20190213162441jpg" /></a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/havelock-island-sightseeing-1188.html">Havelock Island</a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/snorkeling-in-andamans-sightseeing-1195.html"><img alt="Snorkeling in Andamans" src="https://www.holidify.com/images/cmsuploads/thumbnail/4100_20190411095641.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/snorkeling-in-andamans-sightseeing-1195.html">Snorkeling in Andamans</a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/cellular-jail-sightseeing-1184.html"><img alt="Cellular Jail" src="https://www.holidify.com/images/cmsuploads/thumbnail/3616_20190213160612jpg" /></a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/cellular-jail-sightseeing-1184.html">Cellular Jail</a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/rajiv-gandhi-water-sports-complex-sightseeing-1253610.html"><img alt="Rajiv Gandhi Water Sports Complex" src="https://www.holidify.com/images/cmsuploads/thumbnail/a10_20190107123611.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/rajiv-gandhi-water-sports-complex-sightseeing-1253610.html">Rajiv Gandhi Water Sports Complex</a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/ross-island-sightseeing-1192.html"><img alt="Ross Island" src="https://www.holidify.com/images/compressed/thumbnail/3621.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/ross-island-sightseeing-1192.html">Ross Island</a></p>

<hr />
<p><a href="https://www.holidify.com/places/andaman-nicobar-islands/sightseeing-and-things-to-do.html"><strong>View All Places To Visit In Andaman &amp; Nicobar Islands &gt;</strong></a></p>

     """
    },
    {
    "title":"places to be visit in india(leh)",
    "text": """ <ul>
	<li><a href="https://www.holidify.com/places/ladakh/" title="Leh Ladakh Tourism">Overview</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/sightseeing-and-things-to-do.html" title="Places to visit in Leh Ladakh">Places to Visit&nbsp;</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;DestSecondaryHeader&quot;)" title="Hotels in Leh Ladakh">Hotels</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/packages.html" onclick="trackPackageButtonClick(&quot;DestSecondaryHeader&quot;)" title="Leh Ladakh Packages">Packages</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/how-to-reach.html" title="How to reach Leh Ladakh">How to Reach</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/best-time-to-visit.html" title="Best time to visit Leh Ladakh">Best Time To Visit</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/map-view.html" title="Leh Ladakh Tourist Map">Map</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/photos.html" title="Photos of Leh Ladakh">Photos</a></li>
	<li>&nbsp;</li>
	<li><a href="https://www.holidify.com/places/ladakh/restaurants-places-to-eat-local-cuisine.html" title="Restaurants in Leh Ladakh">Food</a></li>
</ul>

<p>&nbsp;</p>

<p><img alt="ladakh photos" src="https://www.holidify.com/images/cmsuploads/thumbnail/zanskar-river-3859214_1920_20190304123111.jpg" title="Zanskar Valley" />&nbsp;<img alt="ladakh photos" src="https://www.holidify.com/images/cmsuploads/thumbnail/Karakoram-West_Tibetan_Plateau_alpine_steppe_20190402182622.jpg" title="" />&nbsp;<img src="https://www.holidify.com/images/bgImages/LADAKH.jpg" /></p>

<p>View 151<br />
photos</p>

<p><a href="https://www.holidify.com/places/ladakh/#" id="wishlistButton" onclick="toggleWishlist('DESTINATION');return false;">&nbsp;Wishlist</a></p>

<p>&nbsp;</p>

<h1>Leh Ladakh</h1>

<p><strong>4.7</strong>&nbsp;/ 5139 votes</p>

<p>&nbsp;<a href="https://www.holidify.com/state/jammu-and-kashmir/">Jammu &amp; Kashmir&nbsp;</a>|&nbsp;<a href="https://www.holidify.com/country/india/">India</a></p>

<p>&nbsp;State rank:&nbsp;1 out of 21&nbsp;<a href="https://www.holidify.com/state/jammu-and-kashmir/top-destinations-places-to-visit.html">Places To Visit In Jammu &amp; Kashmir</a></p>

<p>&nbsp;</p>

<p><strong>₹&nbsp;8,000</strong>&nbsp;onwards<a href="https://www.holidify.com/places/ladakh/packages.html" onclick="trackPackageButtonClick(&quot;DestATFViewPackage&quot;)">&nbsp;(View Packages)</a></p>

<p>Get Customized Package</p>

<p><strong><a href="https://www.holidify.com/places/ladakh/hotels-where-to-stay.html" onclick="trackHotelClick(&quot;DestATFButton&quot;)">View Hotels in Ladakh</a></strong></p>

<hr />
<p>&nbsp;Weather:&nbsp;<img src="https://www.holidify.com/images/logos/weather-icons/partly-cloudy-day" />&nbsp;1&deg; C</p>

<p>&nbsp;Ideal duration:&nbsp;5-7 days</p>

<p>&nbsp;Best time:&nbsp;Jun-Sep&nbsp;(Read More)</p>

<p>&nbsp;Nearest Airport:&nbsp;Leh&nbsp;(Check Flights)</p>

<p>&nbsp;Upcoming:&nbsp;Hemis Festival of Ladakh (and 1 more)&nbsp;<a href="https://www.holidify.com/places/ladakh/best-time-to-visit.html#eventSection">(Read More)</a></p>

<p>Ad</p>

<p>&nbsp;</p>

<h3>&quot;India&#39;s Own Moonland&quot;</h3>

<h2>Leh Ladakh Tourism</h2>

<p>A land like no other with superabundance of attractions to visit and phantasmagoric and fabulous landscapes, amazing people and culture, Ladakh is truly a heaven on Earth.</p>

<p>&nbsp;</p>

<p>Bounded by two of the world&#39;s mightiest mountain ranges, the Great Himalaya and the Karakoram, it lies athwart two other, the Ladakh range and the Zanskar range. Ladakh is mystical in all the spheres it covers, from nature, geography, sceneries to the modest cultures that it fosters. Right from gompas to the sensational momos, the superabundance of attractions to visit makes this city make it heaven on earth. It is said that only in Ladakh can a man sitting in the sun with his feet in the shade suffer from sunstroke and frostbite at the same time.<br />
<br />
For those of us living in the constant confusion about the difference between these twin locations, Leh-Ladakh, here is something that might help you. The state of Jammu and Kashmir is divided into three parts: Jammu, Kashmir, and Ladakh. Ladakh, further is divided into two districts: district Leh, and district Kargil. The former district has a popular town &ldquo;Leh&rdquo;and is a great tourist attraction because of its beautiful monasteries, picturesque locations, and interesting markets defining the culture of the place.</p>

<p><a href="https://www.holidify.com/places/ladakh/">READ MORE</a><strong>Download Leh Ladakh PDF Guide</strong></p>

<p>Free . Works Offline . Share Anywhere</p>

<p>Download Now</p>

<h2>Places to Visit In Leh Ladakh</h2>

<p><a href="https://www.holidify.com/places/ladakh/pangong-lake-sightseeing-2583.html"><img alt="Pangong Lake" src="https://www.holidify.com/images/cmsuploads/thumbnail/2999_20190305160539.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/ladakh/pangong-lake-sightseeing-2583.html">Pangong Lake</a></p>

<p><a href="https://www.holidify.com/places/ladakh/magnetic-hill-sightseeing-2579.html"><img alt="Magnetic Hill" src="https://www.holidify.com/images/cmsuploads/thumbnail/3000_20190507132136.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/ladakh/magnetic-hill-sightseeing-2579.html">Magnetic Hill</a></p>

<p><a href="https://www.holidify.com/places/ladakh/leh-palace-sightseeing-2577.html"><img alt="Leh Palace" src="https://www.holidify.com/images/cmsuploads/thumbnail/attr_1512_20190305141801.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/ladakh/leh-palace-sightseeing-2577.html">Leh Palace</a></p>

<p><a href="https://www.holidify.com/places/ladakh/chadar-trek-sightseeing-8242.html"><img alt="Chadar Trek" src="https://www.holidify.com/images/cmsuploads/thumbnail/attr_wiki_3754_20190429161804.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/ladakh/chadar-trek-sightseeing-8242.html">Chadar Trek</a></p>

<p><a href="https://www.holidify.com/places/ladakh/tso-moriri-sightseeing-2589.html"><img alt="Tso Moriri" src="https://www.holidify.com/images/cmsuploads/thumbnail/4656_20190305174607.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/ladakh/tso-moriri-sightseeing-2589.html">Tso Moriri</a></p>

<p><a href="https://www.holidify.com/places/ladakh/zanskar-valley-sightseeing-8108.html"><img alt="Zanskar Valley" src="https://www.holidify.com/images/cmsuploads/thumbnail/attr_8108_20190306174446.jpg" /></a></p>

<p><a href="https://www.holidify.com/places/ladakh/zanskar-valley-sightseeing-8108.html">Zanskar Valley</a></p>

<hr />
<p><a href="https://www.holidify.com/places/ladakh/sightseeing-and-things-to-do.html"><strong>View All Places To Visit In Leh Ladakh &gt;</strong></a></p>

<h2>Leh Ladakh Packages</h2>

<p>Compare quotes from upto 3 travel agents for free</p>

<ul>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/37189050466_6da8216ca6_b_20190403172235.jpg" />
	<p>Tranquil Leh Sightseeing</p>

	<p><strong>₹ 8,000</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/8213533086_d60a422a89_b_20190403124441.jpg" />
	<p>Amazing Leh with Pangong Stay</p>

	<p><strong>₹ 30,000</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
	<li><img src="https://www.holidify.com/images/cmsuploads/square/dest_wiki_7901_20190206191613jpg" />
	<p>Panoramic Ladakh, Srinagar &amp; Kargil</p>

	<p><strong>₹ 35,000</strong>&nbsp;onwards</p>

	<p>CUSTOMIZE &amp; GET QUOTES</p>
	</li>
</ul>

<hr />
<p><a href="https://www.holidify.com/places/ladakh/packages.html" onclick="trackPackageButtonClick(&quot;DestPackagesWidget&quot;)"><strong>View All Packages for Leh Ladakh &gt;</strong></a></p>

<h2>More on Leh Ladakh</h2>

<hr />
<h2>Ladakh - The Perfect Getaway For An Adventure Ride!</h2>

<hr />
<h2>Innerline Permits in Ladakh</h2>

<hr />
<h2>Restaurants and Local Food in Leh Ladakh</h2>

<hr />
<h2>Itinerary</h2>

<hr />
<h2><a href="https://www.holidify.com/places/ladakh/best-time-to-visit.html">Best time to Visit Leh Ladakh</a></h2>

<hr />
<h2><a href="https://www.holidify.com/places/ladakh/how-to-reach.html#commutingWithin">Commuting within Leh Ladakh</a></h2>

<h2>Related Posts about Leh Ladakh</h2>

<p><a href="https://www.holidify.com/blog/things-to-do-in-leh-ladakh/"><img src="https://www.holidify.com/images/small/36.jpg" />Reasons to visit Ladakh</a></p>

<p><a href="https://www.holidify.com/blog/visit-ladakh-in-winters/"><img src="https://www.holidify.com/images/small/128.jpg" />Why Ladakh is a specialty in Winters</a></p>

<p><a href="https://www.holidify.com/pages/shopping-in-ladakh-431.html"><img src="https://www.holidify.com/images/cmsuploads/thumbnail/Seattle_-_TibetFest_14_20180402111619.jpg" />Shopping In Ladakh - The Exquisite Ladakhi Shopping List You Need</a></p>

<p><a href="https://www.holidify.com/blog/leh-ladakh-travelogue/"><img src="https://www.holidify.com/images/small/151.jpg" />Grandeur of Ladakh: A Travelogue</a></p>

<p><a href="https://www.holidify.com/blog/guide-for-a-motorcycle-trip-to-ladakh/"><img src="https://www.holidify.com/images/small/121.jpg" />Must Read before the Ladakh Bike Trip</a></p>
"""
    },
    {
    "title":" top startups 2017",
    "text":"""<h1>10 Hottest Startups of 2017</h1>

<h2>&nbsp;</h2>

<ul>
	<li>FACEBOOK</li>
	<li>TWITTER</li>
	<li>LINKEDIN</li>
</ul>

<p>BY&nbsp;<a href="https://www.investopedia.com/contributors/68092/">REBECCA MCCLAY</a></p>

<p>&nbsp;</p>

<p>&nbsp;Updated Apr 21, 2019</p>

<p>Every year, thousands of new companies pin their hopes on becoming the next big success story. Most will not achieve the lofty heights of, say, Google or Facebook, but a few will certainly blossom into industry leaders. With innovative products, efficient operations, and strong leadership, they are the companies that will help shape the future.</p>

<p>&nbsp;</p>

<p>Here are ten startups on the radar for 2017.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3>1. CastBox&nbsp;</h3>

<p><a href="http://castbox.fm/" rel="nofollow noopener" target="_blank">CastBox</a>&nbsp;wants to become the &ldquo;YouTube of audio.&rdquo; The company makes a podcast player that also helps users discover new podcasts. Founder Xiaoyu Wang says her goal is to make finding key sections of audio on the web as easy as finding key pieces of text. So far, CastBox has raised $16 million in funding as it plans to launch an audio search feature that processes natural language.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3>2. Slack</h3>

<p>An internal messaging platform,&nbsp;<a href="https://slack.com/" rel="nofollow noopener" target="_blank">Slack</a>&nbsp;has more than 6 million users. Flickr co-founder Stewart Butterfield launched the company in 2013, and it was recently valued at $5 billion. Slack allows company employees to communicate in one place, whether they are working from their office computers or tablets while on the road.</p>

<p>&nbsp;</p>

<h3>3. DigitalOcean</h3>

<p>​<a href="https://www.digitalocean.com/" rel="nofollow noopener" target="_blank">DigitalOcean</a>&nbsp;is a cloud-based host that was founded in 2011 by Ben and Moisey Uretsky. The company has undergone an incredible amount of growth over the past six years. DigitalOcean&nbsp;was named to the Forbes 2017 Cloud 100 list, which are the top 100 private cloud companies in the world.&nbsp;It now serves more than 50,000 companies.</p>

<p>&nbsp;</p>

<p>Not all startups are successful, but these companies all have great ideas and experienced leadership with significant investments for their futures.</p>

<p>&nbsp;</p>

<h3>4. eShares&nbsp;</h3>

<p><a href="http://eshares.com/" rel="nofollow noopener" target="_blank">eShares</a>&nbsp;aims to be a platform that provides privately held companies with their equity needs. Its business serves firms like Slack, Funding Circle, and Flexport by helping them keep track of their shares with its management software. Founded in 2014, eShares recently raised $42 million in Series C funding. With a subscription business model, it works with about 6,000 companies. Its next step is to work with companies in their initial public offering processes.</p>

<p>&nbsp;</p>

<h3>5. Mixpanel</h3>

<p><a href="https://mixpanel.com/" rel="nofollow noopener" target="_blank">Mixpanel</a>&nbsp;helps companies understand how their customers behave while on their websites or mobile apps by providing&nbsp;<a href="https://www.investopedia.com/terms/a/a-b-split.asp">A/B testing</a>&nbsp;tools. The startup wants to give clients the ability to look deeper than just page views and instead see the entire path of their customers. Founded in 2009, Mixpanel is now approaching a billion-dollar valuation.</p>

<p>&nbsp;</p>

<h3>6. Acorns</h3>

<p><a href="https://www.acorns.com/" rel="nofollow noopener" target="_blank">Acorns</a>&nbsp;want to make saving and investing as simple as possible for the average consumer. After connecting users&#39;&nbsp;<a href="https://www.investopedia.com/terms/d/debit.asp">debit</a>&nbsp;and credit cards, the app gives them the ability to round up all purchases to the nearest dollar. The extra amount is then swept into a diversified investment&nbsp;<a href="https://www.investopedia.com/terms/p/portfolio.asp">portfolio</a>. The company was founded in 2012 and is valued at more than $1 billion. It has some 1 million micro-accounts.</p>

<p>&nbsp;</p>

<h3>7. Shyp</h3>

<p><a href="https://www.shyp.com/" rel="nofollow noopener" target="_blank">Shyp</a>, which was founded in 2013 by Jack Smith, Joshua Scott, and Kevin Gibbon, is attempting to take all the stress out of shipping packages. The company will pick up a customer&#39;s items wherever they want, pack them for them, and then ship them for the cheapest price possible. Shyp is currently operational in San Francisco. The company said it wants to prove its business model there before expanding.</p>

<p>&nbsp;</p>

<h3>8. Petuum</h3>

<p><a href="http://www.petuum.com/" rel="nofollow noopener" target="_blank">Petuum</a>&nbsp;aims to help remedy the shortage of machine learning operators with software to facilitate machine learning development. Founded in 2016, the company recently raised $93 million in Series B funding. Petuum says that capital infusion makes it one of the highest-funded early-stage startups working in artificial intelligence and machine learning.</p>

<p>&nbsp;</p>

<h3>9. ClassDojo</h3>

<p><a href="https://www.classdojo.com/" rel="nofollow noopener" target="_blank">ClassDojo</a>&nbsp;is a communication platform that helps connect teachers, students, and parents. Its platform allows teachers to encourage students while engaging with parents about their children&#39;s progress in the classroom. ClassDojo is currently being used in 90 percent of the classrooms in the U.S. Founded in 2011 by Liam Don and Sam Chaudhary, the company has expanded to more than 180 countries.</p>

<p>&nbsp;</p>

<h3>10. Instacart</h3>

<p>​<a href="https://www.instacart.com/" rel="nofollow noopener" target="_blank">Instacart</a>, founded in 2012, is a same-day grocery delivery service. Customers can place an order&nbsp;either online or from their smartphones, and then have it delivered within an hour. The company raised $400 million in funding earlier this year and is now valued at about $3.4 billion.</p>

<p>&nbsp;</p>

<h3>The Bottom Line</h3>

<p>Not all startups will become successful. But the companies listed here all have great ideas and experienced leadership, and have received significant investments for their futures, giving have a distinct leg up over their competition.</p>
 """

    },
    {
    "title":"top 5 it company in india",
    "text":"""<h1>5 top IT companies in India</h1>

<p>Sure, there might be a question of&nbsp;<a href="http://www.nationalskillindiamission.in/news/137/" rel="nofollow" target="_blank">credibility</a>&nbsp;for Indian software engineers, or low hourly rates. Although, in recent years, the IT sector in India has turned into a hub for many global tech companies including HP, Dell, TCS, Infosys, Viacom, Oracle. Indian IT is among top destinations for software outsourcing, serving not just local clients, but&nbsp; reaching out worldwide. After analyzing portfolios, customer reviews, rates and experience, we&rsquo;ve compiled the list of best IT companies in India.</p>

<h2>Top IT companies in India</h2>

<h3><strong>#1&nbsp;<a href="https://www.resourcology.com/" rel="nofollow" target="_blank">Resourcology</a></strong></h3>

<p>Resourcology is one of the fastest growing IT Company in India and across the Anglosphere. Established in 2016 with their offices in India and Canada, they provide an array of state-of-the-art IT solutions and innovations to clients ranging from SMB&rsquo;s to Fortune 500 companies. Accenture, ProSAP, Xerox, Whirlpool, British Council are some of their most prominent clients. They focus on the value that they provide to their clients. Before commencing any project, they offer a free consultation so that the clients can decide after they have worked briefly with the Resourcology team.</p>

<p><img alt="" src="https://static.thinkmobiles.com/uploads/2018/06/Resourcology--1024x446.png" style="height:446px; width:1024px" /><br />
<strong>Specialties:</strong>&nbsp;Web development, App development, Software development, UX design, QA<br />
<strong>Hourly rate</strong>: $20 -$50/&nbsp;<strong>Headquarters</strong>: Ontario, Canada/&nbsp;<strong>Founded</strong>: 2016/<strong>&nbsp;Employees</strong>: 120/&nbsp;<strong>Contact</strong>: +1 213 394 3344.</p>

<p><strong>Website:&nbsp;</strong><a href="https://www.resourcology.com/" rel="nofollow" target="_blank">https://www.resourcology.com/</a></p>

<h3><strong>#2&nbsp;</strong><strong><a href="https://magnetoitsolutions.com/" rel="nofollow" target="_blank">Magneto IT Solutions</a></strong></h3>

<p>Founded in 2009, we at Magneto work with passion to bring your ideas to life and create stunning applications for start-up and corporate. We mainly focus on eCommerce, Mobile Application, Customize Web Application, IOT, Chatbot. We understand professional service as an opportunity to walk on the path of values. Every day is a fresh challenge to adhere to our essential milestone principles. From our beginning in 2009, we have been pursuing a set of values as definitive guidelines of providing quality service.</p>

<p><img alt="IT development company MAgento" src="https://static.thinkmobiles.com/uploads/2018/06/it-company-in-india-magento.jpg" style="height:645px; width:1349px" /></p>

<p><strong>Specialties</strong>: eCommerce Development, Web Development, Mobile App Development, Chatbot Development, IoT Development, Digital Marketing Services</p>

<p><strong>Hourly rate</strong>: $15/ Headquarters: India, USA, Bahrain /&nbsp;<strong>Founded</strong>: 2009 /&nbsp;<strong>Employees</strong>: 100/&nbsp;<strong>Contact</strong>: +1 214 447 0720 , +91-8141301021</p>

<p><strong>Website</strong>:&nbsp;<a href="https://magnetoitsolutions.com/" rel="nofollow" target="_blank">https://magnetoitsolutions.com</a></p>

<h3><strong>#3&nbsp;<a href="https://www.webcluesinfotech.com/" rel="nofollow" target="_blank">WebClues Infotech</a></strong></h3>

<p>WebClues Infotech is a web and mobile development solutions provider that started its way in 2014 in Ahmedabad, India. This company has already implemented over 1, 200 of web development projects by providing customized web solutions, web hosting and web design.<br />
The team of professionals constructs websites which are search engine friendly, develops pages with the dynamic interfaces and designs custom plugins that could be integrated on the client&rsquo;s website.</p>

<p><img alt="" src="https://static.thinkmobiles.com/uploads/2018/06/web-1024x500.jpg" style="height:500px; width:1024px" /></p>

<p><strong>Specialties</strong>: web development, mobile app development, web designing and e-commerce development.</p>

<p><strong>Hourly rate:&nbsp;</strong>$15 /&nbsp;<strong>Headquarters</strong>: Ahmedabad, India/&nbsp;<strong>Employees</strong>:150 /&nbsp;<strong>Contact:&nbsp;</strong>sales@webcluesinfotech.com<br />
<strong>Website</strong>:&nbsp;<a href="https://www.webcluesinfotech.com/" rel="nofollow" target="_blank">https://www.webcluesinfotech.com/</a></p>

<h3><strong>#4 Appentus</strong></h3>

<p>Appentus Technologies is a mobile app and web development company with branches in India, UK, USA and UAE.&nbsp;For years now, they have built the reputation as one of the best B2B providers for agencies, startups and even Fortune 500 companies. The goal of Appentus Technologies is not necessarily to have a large client base but to maintain a customer-friendly environment. So as to give life to ideas and, thus, shape their future into what they desire. The company also addresses and provides IT solutions for various sectors such as manufacturing, education, healthcare, logistics, financial institutions.</p>

<p><img alt="list of Indian IT companies" src="https://static.thinkmobiles.com/uploads/2018/06/appentus.jpg" style="height:412px; width:800px" /></p>

<p><strong>Specialties</strong>: mobile apps (iOS, Android, iPad, Ionic, iBeacon), web development (Angular, Node, PHP, Laravel, Joomla, magento, WordPress, Drupal), blockchain development.</p>

<p><strong>Hourly rate:&nbsp;</strong>$25 &ndash; $49 /&nbsp;<strong>Headquarters</strong>: Jaipur, India /&nbsp;<strong>Founded</strong>: 2010 /&nbsp;<strong>Employees</strong>: 96 /&nbsp;<strong>Contact&nbsp;</strong>+919116645020</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.appentus.com/" rel="nofollow" target="_blank">https://www.appentus.com</a></p>

<h3><strong>#5 Trigent</strong></h3>

<p>After more than two decades of experience and hundreds of delivered products, Trigent occupies a leading position among the top IT companies in India. HP, Honeywell, Oracle, Clarks Emerson and other global players from manufacturing, transportation, financial, healthcare and insurance, and eCommerce industries are partnered with Trigent to get end-to-end software development. Providing offshore software development, Trigent was more than once named by Clutch as a global leader, top IT services company and top software provider during the past few years.</p>

<p><strong>Specialties</strong>: cloud development and transformation, QA and testing, SharePoint services, enterprise digital transformation, product engineering, business intelligence, enterprise ADM, mobile app development, SaaS.</p>

<p><strong>Hourly rate:&nbsp;</strong>$25 &ndash; $49 /&nbsp;<strong>Headquarters</strong>: Khanija Bhavan, India /&nbsp;<strong>Founded</strong>: 1995 /&nbsp;<strong>Employees</strong>: 686 /&nbsp;<strong>Contact&nbsp;</strong>+918022263000</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.trigent.com/" rel="nofollow" target="_blank">https://www.trigent.com/</a></p>

<p><img alt="outsourcing companies India" src="https://static.thinkmobiles.com/uploads/2018/06/trigent.jpg" style="height:437px; width:800px" /></p>
 """
    },
    {
    "title":"IT companies in india",
    "text":""" <h3><strong>#6 Confianz Global</strong></h3>

<p>Confianz Global plays a notable role in the Indian IT market. With offices in both eastern and western hemispheres, they develop software products for such companies as AT&amp;T, Short Run Pro, Toledo Zoo, Apptega, Killarney Metals and others. Besides offering package services in ERP, custom mobile and web app development, a significant part of their occupation are Odoo supplying products. They are specialised in Odoo customization, implementation, and Odoo app development.</p>

<p><strong>Specialties</strong>: Odoo Implementation, mobile app development, web app development, outsourced product development, Big Data analytics.</p>

<p><strong>Hourly rate:&nbsp;</strong>$50 &ndash; $99 /&nbsp;<strong>Headquarters</strong>: Trivandrum, India /&nbsp;<strong>Founded</strong>: 2008 /&nbsp;<strong>Employees</strong>: 55 /&nbsp;<strong>Contact&nbsp;</strong>&nbsp;+914714015750</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.confianzit.com/" rel="nofollow" target="_blank">https://www.confianzit.com/</a></p>

<h3><strong>#7 Endive Software</strong></h3>

<p>Ten years experience and more than thousands of clients behind, Endive Software earned a name as one of the top IT companies in India. The company deliver services for the automobile (Audi, Ford, Mahindra), beauty and wellness (Hugo Boss, Johnsons &amp; Johnsons), real estate, travel, social media, education, logistics and banking industries. As for the preferred technology to work with, Endive Software developers build on PHP, Laravel, CakePHP, Symphony, Magneto, Node.JS, Drupal, Joomla, Ruby on Rails. Being an official Salesforce partner, Endive is also able to develop, implement, integrate product and solutions on this CRM platform.</p>

<p><strong>Specialties</strong>: mobile app development, UI/UX, web development and responsive web design, Oracle ERP implementation, CRM development, eCommerce web development, digital marketing services.</p>

<p><strong>Hourly rate:&nbsp;</strong>$25 &ndash; $49 /&nbsp;<strong>Headquarters</strong>: Jaipur, India /&nbsp;<strong>Founded</strong>: 2006 /&nbsp;<strong>Employees</strong>: 61 /&nbsp;<strong>Contact&nbsp;</strong>+918529006667</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.endivesoftware.com/" rel="nofollow" target="_blank">https://www.endivesoftware.com/</a></p>

<h3><strong>#8 Wildnet Technologies</strong></h3>

<p>For good reason, Wildnet is on the list of top IT companies in India. Best known for its creative approach to web/mobile app development and UI/UX design, it is named as Deloitte Fast 50 India Technology and Fast 500 Asia Technology in 2014/2015.</p>

<p>For iOS, Android, Windows and hybrid app development, company&rsquo;s IT specialists work upon Unity 3D, Corona, Sencha, Xamarin, Appcelerator, React Native, Jquery Mobile, Corodova and Salesforce Mobile App technologies, AWS and &nbsp;Microsoft Azure cloud platforms. As a bonus, Wildnet Technologies&rsquo; products are well equipped with all digital marketing tools &ndash; SEO, Pay Per Click services and social media marketing.</p>

<p><strong>Specialties</strong>: custom mobile app development, UI/UX design, CRM migration, &nbsp;Salesforce customization and migration, cloud computing, enterprise app development, Smart TV app development, Blockchain, QA and testing, digital marketing, enterprise integration.</p>

<p><strong>Hourly rate:&nbsp;</strong>&lt; $25 /&nbsp;<strong>Headquarters</strong>: Jaipur, India /&nbsp;<strong>Founded</strong>: 2008 /&nbsp;<strong>Employees</strong>: 551 /&nbsp;<strong>Contact&nbsp;</strong>&nbsp;+911204533500</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.wildnettechnologies.com/" rel="nofollow" target="_blank">https://www.wildnettechnologies.com/</a></p>

<p><img alt="top tech companies of India" src="https://static.thinkmobiles.com/uploads/2018/06/wildnet.jpg" style="height:357px; width:800px" /></p>

<h3><strong>#9 Tata Consultancy Services Ltd.</strong></h3>

<p>The first software service provider in India. The company with revenue of $19.09 billion in 2017. One of 10 world&rsquo;s largest IT services firms. And all these statements are about Tata Consultancy Services Ltd. Worldwide-recognized brand, TCS offers quality engineering, business operations, consulting and systems integration, engineering, technology operations solutions and services. They partnered with leaders from banking and financial, communications and media, manufacturing, retail, HiTech and travel industries. Among their products, the most efficient for business are CHROMA, ignio, TCS iON, TAP, TCS MasterCraft, Customer Intelligence &amp; Insights, Intelligent Urban Exchange, Optumera, TCS BaNCS, and platforms Advanced Drug Development, Connected Intelligence Platform, ERP on Cloud, HOBS and TCS Cloud Plus.</p>

<p><strong>Specialties</strong>: IT services, business solutions, consulting, Artificial Intelligence, Big Data, Cloud computing, Cyber Security, IoT.</p>

<p><strong>Headquarters</strong>: Mumbai, India /&nbsp;<strong>Founded</strong>: 1968 /&nbsp;<strong>Employees</strong>: 366 339 /&nbsp;<strong>Contact&nbsp;</strong>&nbsp;++91226778 9999</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.tcs.com/" rel="nofollow" target="_blank">https://www.tcs.com/</a></p>

<h3><strong>#10 Infosys</strong></h3>

<p>Another one global leader on our list of top IT companies in India. The Infosys&rsquo; main goal is to assist their client in the digital transformation of business. They always emphasize on how AI-powered core and agile-scale technologies can improve all sides of the business. And that is why the company&rsquo;s priority is delivering next-generation digital products. Infosys with all its subsidiary, like Infosys BPM, provides end-to-end solutions for a variety of business areas. For implementation digital solutions, the company supplies clients with different platforms. For example, Infosys Nia is an AI platform for process automatization, EdgeVerve is made mostly for banking and interactive commerce services, Panaya for fast application delivery and Skava for mobile commerce.</p>

<p><strong>Specialties</strong>: IT solutions and services, products and platforms, engineering services, Cloud services, AI, Digital, Big Data, Blockchain, business applications.</p>

<p><strong>Hourly rate:&nbsp;</strong>&lt;$25/&nbsp;<strong>Headquarters</strong>: Bangalore, India /&nbsp;<strong>Founded</strong>: 1981 /&nbsp;<strong>Employees</strong>: 207 666 /&nbsp;<strong>Contact&nbsp;</strong>&nbsp;++91226778 9999</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.infosys.com/" rel="nofollow" target="_blank">https://www.infosys.com/</a></p>

<h3><strong>#11 Clarion Technologies</strong></h3>

<p>Being one of the best IT outsourcing companies, Clarion Technologies builds solutions for clients from North America and Europe, from start-ups to big enterprises. With most welcoming industries like manufacturing, education, construction, healthcare, telecom, media and retail, this IT provider helps to cope with all digital tasks and requirements. Clarion team of dedicated developers is a key of successes: in their work, they use a variety of most powerful technologies and tools. For example, for web development ( CMS, apps, eCommerce platforms) it will be PHP, .NET, Python, Joomla, Shopify, Java, and Microsoft Azure, AWS, Docker, Puppet, Chef and Jenkins are used for cloud migration and cloud application development.</p>

<p><strong>Specialties</strong>: web development, CMS, application maintenance, eCommerce, QA, offshore product development, cloud computing, software testing services, information security.</p>

<p><strong>Hourly rate:&nbsp;</strong>$25 &ndash; $49 /&nbsp;<strong>Headquarters</strong>: Pune, India /&nbsp;<strong>Founded</strong>: 2000 /&nbsp;<strong>Employees</strong>: 520 /&nbsp;<strong>Contact&nbsp;</strong>+912049007000</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.clariontech.com/" rel="nofollow" target="_blank">https://www.clariontech.com/</a></p>

<h3><img alt="list of Indian IT companies" src="https://static.thinkmobiles.com/uploads/2018/06/clarion.jpg" style="height:355px; width:800px" /></h3>

<h3><strong>#12 Wipro</strong></h3>

<p>Award-winning company with a unique approach to transforming and integrate the business into the digital environment. Focused on strategy, design and technology, Wipro offers task-solving tools for a wide range of businesses: banking, consumer electronics, healthcare, aerospace, engineering and construction, network equipment providers, pharmaceutical, retail and many others. The IT company shows interests and big experience in app development, in providing cloud and infrastructure services, product engineering and analytics. Wipro creates and launches an as-a-Service solution, powered by automation, advanced analytics, Cloud, security, social and other emerging digital technologies, and able to ensure agility, flexibility, standardization for enterprises.</p>

<p><strong>Specialties</strong>: Big Data, Blockchain, Cloud, Cyber Security and &nbsp;enterprise risk, DevOps, enterprise architecture, enterprise ops transformation, Industry 4.0, IoT, mobility, open source, product lifecycle management.</p>

<p><strong>Headquarters</strong>: Bangalore, India /&nbsp;<strong>Founded</strong>: 1945 /&nbsp;<strong>Employees</strong>: 175 926 /&nbsp;<strong>Contact&nbsp;</strong>+918028440011</p>

<p><strong>Website</strong>&nbsp;<a href="https://www.wipro.com/" rel="nofollow" target="_blank">https://www.wipro.com/</a></p>

<h3><strong>#13 Ideas2IT Technologies</strong></h3>

<p>Another honourable member of the list of top IT companies in India. Since its entering the market ten years ago, Ideas2IT has been growing and developing into a novation associate for Microsoft, Ericsson, IdeaMed, Motorola, eBay, AirAsia. Working with healthcare, retail, financial and marketing companies, Ideas2IT became an expert in mobile, frontend and full stack development, and also machine learning. As for the technologies, the most familiar to work with are Java, Ruby, Rails, Node.js, MongoDB, Tableau and more.</p>

<p><strong>Specialties</strong>: Big Data, Frontend, mobile applications, Chatbot, Data Analytics, Data Science, DevOps, Cloud deployment.</p>

<p><strong>Hourly rate:&nbsp;</strong>$25 &ndash; $49 /&nbsp;<strong>Headquarters</strong>: Chennai, India /&nbsp;<strong>Founded</strong>: 2008 /&nbsp;<strong>Employees</strong>: 239 /&nbsp;<strong>Contact&nbsp;</strong>+914443589625</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.ideas2it.com/" rel="nofollow" target="_blank">https://www.ideas2it.com/</a></p>

<h3><strong>#14 HCL Technologies</strong></h3>

<p>HCL Technologies like nobody else will help to transform and shift businesses into a new digital environment. Being among the top IT companies in India, HCK has offices in 39 countries, in both Americas, Europe, Middle East and Africa. In early 90th the company was lucky enough to launch a few know-how, and since then they play a significant role in the IT sphere.</p>

<p>With annual revenue in more than $7.8 billion, HCL Technologies provides services for the leading members of the Fortune 500 and Global 2000 across such industries like aerospace and defence, automotive, banking, capital markets, Hi-Tech, manufacturing, retail, travel, transport, logistics and hospitality. In pursuit of advanced services, they offer Mode 1-2-3 strategy, based digitalization, analytics, Cloud, IoT and Cybersecurity, and which helps enterprises to integrate with next-generation technologies.</p>

<p><strong>Specialties</strong>: application development and maintenance, software engineering, product testing, finance and accounting services, digital and content services, cloud-native services, cyber-security.</p>

<p><strong>Headquarters</strong>: Noida, India /&nbsp;<strong>Founded</strong>: 1991 /&nbsp;<strong>Employees</strong>: 119 897 /&nbsp;<a href="https://www.hcltech.com/contact-us/customer" rel="nofollow" target="_blank"><strong>Contact</strong></a></p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.hcltech.com/" rel="nofollow" target="_blank">https://www.hcltech.com/</a></p>

<p><img alt="best software agencies in India" src="https://static.thinkmobiles.com/uploads/2018/06/hcl.jpg" style="height:404px; width:800px" /></p>

<h3><strong>#15 TechJini</strong></h3>

<p>Today, having web and mobile presence is the vital requirements for the successful business. And TechJini helps to get original and recognizable applications. Focused on product engineering, application development and its maintenance, the company&rsquo;s specialists became good Jinns for such companies as Honeywell, Lacoste, Redbox, Flipkart, Jda, Avista Corp, Auchan and many more. Besides app development for iOS, Android and Microsoft, TechJini delivers cloud solutions, digital platform development, UI/UX design and prototyping, and works on implementation innovation technologies into the clients&rsquo; business.</p>

<p><strong>Specialties</strong>: product engineering, mobile app development, web application development, UI/UX, user-centered design, Virtual Reality, digital transformation services and consulting.</p>

<p><strong>Hourly rate:&nbsp;</strong>$25 &ndash; $49 /&nbsp;<strong>Headquarters</strong>: Bangalore, India /&nbsp;<strong>Founded</strong>: 2005 /&nbsp;<strong>Employees</strong>: 297 /&nbsp;<strong>Contact&nbsp;</strong>+918042103414</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.techjini.com/" rel="nofollow" target="_blank">https://www.techjini.com/</a></p>
"""
    },
    {
    "title":"IT Companies",
    "text":""" <h3><strong>#16 Tech Mahindra</strong></h3>

<p>Being a part of the Mahindra Group, it is not surprising, that Tech Mahindra easily became one of the top IT companies in India. With a more intense emphasis on the delivering services for the telecommunications industry, the company also works with banking, financial, insurance, communication, media and entertainment, energy and utilities, Hi-Tech, healthcare, manufacturing, retail and transportation areas.</p>

<p>To drive and boost business into the new digital era, Tech Mahindra practices customer-centric technologies and tools, and provides highly-integrated and flexible platforms: CareXa (NexGen Customer Care), SOCIO(social media management), UNO (Robotic Process Automation), PRISM, FQCC, CAP (Cloud Aggregation Platform) and others.</p>

<p><strong>Specialties</strong>: cloud, customer experience, enterprise architecture, DevOps, analytics and connected enterprise solutions, integrated engineering, infrastructure management services, mobility services, network services, enterprise security and risk management.</p>

<p><strong>Headquarters</strong>: Pune, India /&nbsp;<strong>Founded</strong>: 1986 /&nbsp;<strong>Employees</strong>: 81 988 /&nbsp;<strong>Contact&nbsp;</strong>+912049007000</p>

<p><strong>Website</strong>:&nbsp;<a href="http://techmahindra.com/" rel="nofollow" target="_blank">http://techmahindra.com/</a></p>

<h3><strong>#17 Mphasis</strong></h3>

<p>For the last two decades, Mphasis was doing a remarkable work on business integration with cloud and cognitive technologies and helped enterprises to reach a new level of digital transformation. Among the company&rsquo;s clients, there are leaders from banking and capital markets, insurance, communication, energy and utilities, healthcare, life sciences. Mphasis X2C framework- what is the reason the company became one of the top IT companies in India. In collaboration with Front2Back&trade;, it became an ultimate tool for fast digital alteration and advanced personalization of business infrastructure, with minimal breaking already existing systems.</p>

<p><strong>Specialities</strong>: cloud infrastructure, digital marketing, Big Data and analytics, Data management, cloud app development, DevOps, API management, cognitive computing platform, robotic process automation, product engineering.</p>

<p><strong>Headquarters</strong>: Bangalore, India /&nbsp;<strong>Founded</strong>: 1998 /&nbsp;<strong>Employee</strong>/ 28 471&nbsp;<strong>Contact&nbsp;</strong>+914466370000</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.mphasis.com/" rel="nofollow" target="_blank">https://www.mphasis.com/</a></p>

<p><img alt="information technology companies India" src="https://static.thinkmobiles.com/uploads/2018/06/mphasis.jpg" style="height:395px; width:800px" /></p>

<h3><strong>#18 Mindtree</strong></h3>

<p>Mindtree has delivered next-generation technologies to world leaders like Honeywell, Purina, GlaxoSmithKline, The Carlyle Group and others from the &nbsp;Global 2000 list. This IT provider became known as one of the top IT companies in India due to its ability to solve digital tasks of any complexity. Banking, capital markets, education, manufacturing, retail, transportation and logistics, smart devices &ndash; if you run your business in one of these industries, you are more than welcomed to collaborate with Mindtree. The company grows fast but not to the detriment of quality. Mindtree has launched such ultimate products for enterprise transformation like Flooresense for in-store analytics, Gladius as a video management and analytics software, and Digital Pumpkin, a digital innovation hub.</p>

<p><strong>Specialties</strong>: infrastructure management services, mobility, independent testing, analytics and information management, cloud computing, Data analytics, digital commerce, digital marketing, application and infrastructure optimization.</p>

<p><strong>Headquarters</strong>: Bangalore, India /&nbsp;<strong>Founded</strong>: 1999 /&nbsp;<strong>Employees</strong>: 22 303 /&nbsp;<strong>Contact&nbsp;</strong>+918067064000</p>

<p><strong>Website</strong>: &nbsp;<a href="https://www.mindtree.com/" rel="nofollow" target="_blank">https://www.mindtree.com/</a></p>

<h3><strong>#19 ThinkPalm Technologies</strong></h3>

<p>Still pretty young IT company, ThinkPalm Technologies became a global vendor of enterprise, mobility and communication solutions. If look closely at their previous experience, you can find such names as Royal Arabian, Scorpio, All Day Safety Services, Synergy Marine Group, Riverbed Technology, Drobo and others. Focused on telecom, retail, media and entertainment, and manufacturing industries, ThinkPalm has launched a few products, able to bring end-to-end enterprise mobility services. Those are Q-Aud for mobile audit, Astra, a tracking software, Palm BI, Big Data framework, Think Tax, Avishkar, NetShack and others.</p>

<p><strong>Specialties</strong>: enterprise IT, mobile app development, IoT, DevOps, SDN, NFV, cloud computing, firmware development, machine learning, product engineering, business intelligence frameworks, enterprise apps.</p>

<p><strong>Hourly rate:&nbsp;</strong>$25 &ndash; $49 /&nbsp;<strong>Headquarters</strong>: Kochi, India /&nbsp;<strong>Founded</strong>: 2010 /&nbsp;<strong>Employees</strong>: 287 /&nbsp;<strong>Contact&nbsp;</strong>+914844104100</p>

<p><strong>Website</strong>:&nbsp;<a href="http://www.thinkpalm.com/" rel="nofollow" target="_blank">http://www.thinkpalm.com/</a></p>

<h3><strong>#20 Hexaware Technologies</strong></h3>

<p>Almost 30 years of experience make Hexaware Technologies one of the leading IT companies not just in India but in the whole world. Determine themselves as a next-generation provider, they have been focusing on automatization, cloud integration and digital transformation of clients&rsquo; businesses. Hexaware launched a few platforms able to manage banking and financial services, travel and transportation, healthcare and insurance, manufacturing industries like Orchestrate IT and iD2E. For example, RAISE IT provides automation processes, H2O Platform is a service management with a scalable and intuitive interface.</p>

<p><strong>Specialties</strong>: application transformation management, application support and maintenance, business intelligence and analytics, business process services, digital assurance, digital customer enterprise solutions, infrastructure management services, customer experience transformation.</p>

<p><strong>Headquarters</strong>: Navi Mumbai, India /&nbsp;<strong>Founded</strong>: 1990 /&nbsp;<strong>Employees</strong>: 12 571 /&nbsp;<strong>Contact&nbsp;</strong>+9102267919595</p>

<p><strong>Website</strong>:&nbsp;<a href="https://hexaware.com/" rel="nofollow" target="_blank">https://hexaware.com/</a></p>

<p><img alt="top it companies in India 2018" src="https://static.thinkmobiles.com/uploads/2018/06/hexaware.jpg" style="height:354px; width:800px" /></p>

<h3><strong>#21 KPIT Technologies</strong></h3>

<p>Since its beginning, KPIT Technologies show themselves as a strong competitor in providing &nbsp;IT services and product engineering solutions. Dealing with representatives from automotive and transportation, energy and resources, High Tech, life sciences and utility industries, KPIT is focused on offering customer-focused, innovative, agile, sustainable and safe products. And as for the trust issues to the company, such automobile titans like Jaguar, Land-Rover, Volvo, Ford, Tata, Eicher already have implemented KPIT solutions.</p>

<p><strong>Specialities</strong>: business technology services, IT services, product engineering, embedded systems development, enterprise software support, software solutions.</p>

<p><strong>Headquarters</strong>: Pune, India /&nbsp;<strong>Founded</strong>: 1990 /&nbsp;<strong>Employees</strong>: 13 044 /&nbsp;<strong>Contact&nbsp;</strong>+912066525000</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.kpit.com/" rel="nofollow" target="_blank">https://www.kpit.com/</a></p>

<h3><strong>#22 Sasken</strong></h3>

<p>Founded in 1989 and based in the centre of Silicon Valley of India, Sasken became a known specialist in product engineering and providing digital transformation solutions. Their key offerings are hardware design and development, device and platform testing, IC design, multi-domain controller, Smart Mobility and application development. Currently, Sasken has its offices in India, Finland, China, Germany, Japan, UK and USA, 70 patents and already has delivered projects to more than a hundred companies from Fortune 500.</p>

<p><strong>Specialties</strong>: electronic design, mechanics design, connectivity, firmware, RF design, production testing, analytics, cross-platform technologies.</p>

<p><strong>Headquarters</strong>: Bengaluru, India /&nbsp;<strong>Founded</strong>: 1989 /&nbsp;<strong>Employees</strong>: 3 523 /&nbsp;<strong>Contact&nbsp;</strong>+918066943000</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.sasken.com/" rel="nofollow" target="_blank">https://www.sasken.com/</a></p>

<p><img alt="top 20 it companies India" src="https://static.thinkmobiles.com/uploads/2018/06/sasken.jpg" style="height:430px; width:800px" /></p>

<h3><strong>#23 Cybage</strong></h3>

<p>The list of top IT companies in India won&rsquo;t be full without Cybage. The company specialised in providing risks-off digital solutions. Working with cutting-edge and cloud computing technologies, Cybage helps to simplify the process of digital transformation and implement in day-to-day routine new generation tools. Who will win from collaboration with this IT service vendor? For sure, the industries like media and entertainment, travel and hospitality, online retail, healthcare. &nbsp;</p>

<p><strong>Specialities</strong>: IT services, offshore software development, outsourced product development, CRM, enterprise content management, SCM, business intelligence, enterprise mobility.</p>

<p><strong>Headquarters</strong>: Pune, India /&nbsp;<strong>Founded</strong>: 1995 /&nbsp;<strong>Employees</strong>: 7 283 /&nbsp;<strong>Contact&nbsp;</strong>+912066041700</p>

<p><strong>Website</strong>:&nbsp;<a href="http://www.cybage.com/" rel="nofollow" target="_blank">http://www.cybage.com/</a></p>

<h3><strong>#24 Datamatics Global Services</strong></h3>

<p>Award-winning and recognised by international organizations. Its offices are spread over India, Australia, Philippines, UK, Switzerland, UAE and USA. Datamatics Global Services is not only one of the top IT companies in India but, fairly, one of the global leaders. Their innovative approach is based on implementation five technologies: Robotics, Artificial Intelligence, Cloud, Mobility and Advanced Analytics. This gives an ultimate power to boost productivity, increase speed and improve accuracy, and comfort the transformation into the digital environment.</p>

<p><strong>Specialties</strong>: engineering, embedded services, finance and accounting services, information management, IT consulting, IT services, research and analytics, resource augmentation, smart document processing, billing and payment Solutions, online retail solutions, robotic process automation, cloud services, AI.</p>

<p><strong>Headquarters</strong>: Mumbai, India /&nbsp;<strong>Founded</strong>: 1975 /&nbsp;<strong>Employees</strong>: 6 138 /&nbsp;<strong>Contact&nbsp;</strong>+91226102000009</p>

<p><strong>Website</strong>:&nbsp;<a href="https://www.datamatics.com/" rel="nofollow" target="_blank">https://www.datamatics.com/</a></p>
"""
    },
    {
    "title":" home decor",
    "text": """ <h1>Home Decor</h1>

<ul>
	<li>
	<p><a href="https://www.architecturaldigest.com/gallery/how-to-display-family-photos" tabindex="-1">16</a></p>
	<a href="https://www.architecturaldigest.com/gallery/how-to-display-family-photos" tabindex="-1"><img alt="Here’s How Display Those Old Family Photos" src="https://media.architecturaldigest.com/photos/56f1cb234436c4c3624ede1c/16:9/w_768/family-pictures-gallery-wall-ideas-02.jpg" title="" /></a>

	<p>March 2, 2018</p>

	<p>DECORATING</p>

	<p><a href="https://www.architecturaldigest.com/gallery/how-to-display-family-photos">Here&rsquo;s How Display Those Old Family Photos</a></p>
	This is a slideshow with 16 slides</li>
	<li>
	<p>&nbsp;</p>
	<a href="https://www.architecturaldigest.com/story/affordable-art-online" tabindex="-1"><img alt="A series of artworks from Minted." src="https://media.architecturaldigest.com/photos/57759ccd0cfd25cd2798eba2/16:9/w_768/where-to-buy-art-online-05.jpg" title="" /></a>

	<p>February 2, 2018</p>

	<p>BRIGHT IDEAS</p>

	<p><a href="https://www.architecturaldigest.com/story/affordable-art-online">Here&rsquo;s Where to Buy Affordable Art Online</a></p>
	</li>
	<li>
	<p><a href="https://www.architecturaldigest.com/gallery/how-to-outdoor-fire-pit-ideas" tabindex="-1">6</a></p>
	<a href="https://www.architecturaldigest.com/gallery/how-to-outdoor-fire-pit-ideas" tabindex="-1"><img alt="Transform Your Outdoor Fire Pit into a Stylish Hangout" src="https://media.architecturaldigest.com/photos/57a24d4ba065cffc07e866f9/16:9/w_768/outdoor-fire-pit-ideas-02.jpg" title="" /></a>

	<p>December 29, 2017</p>

	<p>HEAT THINGS UP</p>

	<p><a href="https://www.architecturaldigest.com/gallery/how-to-outdoor-fire-pit-ideas">Transform Your Outdoor Fire Pit into a Stylish Hangout</a></p>
	This is a slideshow with 6 slides</li>
	<li>
	<p>&nbsp;</p>
	<a href="https://www.architecturaldigest.com/story/tom-hanks-stephen-colbert-christmas-tree-decorating" tabindex="-1"><img alt="Here's the Refined Strategy Tom Hanks Has for Decorating a Christmas Tree  " src="https://media.architecturaldigest.com/photos/5a314801cf0d6c31eb82ebff/16:9/w_768/111700_0419.jpg" title="" /></a>

	<p>December 13, 2017</p>

	<p>CELEBRITY HOMES</p>

	<p><a href="https://www.architecturaldigest.com/story/tom-hanks-stephen-colbert-christmas-tree-decorating">Here&#39;s the Refined Strategy Tom Hanks Has for Decorating a Christmas Tree</a></p>
	</li>
	<li>
	<p><a href="https://www.architecturaldigest.com/gallery/kitchen-gadgets-everyone-wants-this-season" tabindex="-1">10</a></p>
	<a href="https://www.architecturaldigest.com/gallery/kitchen-gadgets-everyone-wants-this-season" tabindex="-1"><img alt="10 Kitchen Gadgets Everyone Wants This Season" src="https://media.architecturaldigest.com/photos/5a1c8b0d5efa310c49f68ea6/16:9/w_768/kitchen-gifts-smeg.gif" title="" /></a>

	<p>November 27, 2017</p>

	<p>RETAIL THERAPY</p>

	<p><a href="https://www.architecturaldigest.com/gallery/kitchen-gadgets-everyone-wants-this-season">10 Kitchen Gadgets Everyone Wants This Season</a></p>
	This is a slideshow with 10 slides</li>
</ul>

<ul>
	<li>
	<p>&nbsp;</p>
	<a href="https://www.architecturaldigest.com/story/how-to-cleaning-leather-furniture" tabindex="-1"><img alt="RH's Cloud Sectional in Pewter Italian Milano Leather." src="https://media.architecturaldigest.com/photos/57b4d0728714e5ff1d20b158/16:9/w_768/leather-furniture-care-01.jpg" title="" /></a>

	<p>November 10, 2017</p>

	<p>GOOD AS NEW</p>

	<p><a href="https://www.architecturaldigest.com/story/how-to-cleaning-leather-furniture">How to Take Care of Your Leather Furniture</a></p>
	</li>
	<li>
	<p>&nbsp;</p>
	<a href="https://www.architecturaldigest.com/story/shou-sugi-ban-black-waterproof-wood-furniture" tabindex="-1"><img alt="Shou Sugi Ban technique" src="https://media.architecturaldigest.com/photos/59fca561f0511d186d921048/16:9/w_768/shou-sugi-ban-brush-1.gif" title="" /></a>

	<p>November 3, 2017</p>

	<p>TIME TO DIY</p>

	<p><a href="https://www.architecturaldigest.com/story/shou-sugi-ban-black-waterproof-wood-furniture">Use This Incredible Technique to Waterproof Wood Furniture</a></p>
	</li>
	<li>
	<p>&nbsp;</p>
	<a href="https://www.architecturaldigest.com/story/brooklyn-loft-renovation-new-affiliates" tabindex="-1"><img alt="Loft space by New Affiliates" src="https://media.architecturaldigest.com/photos/59f77ad42e2bd8794206e5df/16:9/w_768/bed-stuy-loft-new-affiliates-2.jpg" title="" /></a>

	<p>October 31, 2017</p>

	<p>BEFORE + AFTER</p>

	<p><a href="https://www.architecturaldigest.com/story/brooklyn-loft-renovation-new-affiliates">This Gorgeous Loft Reno Makes Magic From Everyday Raw Materials</a></p>
	</li>
	<li>
	<p>&nbsp;</p>
	<a href="https://www.architecturaldigest.com/story/book-cloth-is-secretly-amazing-for-home-decor" tabindex="-1"><img alt="That Fabric on Hardcover Books Is Secretly Amazing for Home Decor" src="https://media.architecturaldigest.com/photos/59f0defc364d3439f251b0e0/16:9/w_768/bookcloth-marianna-kennedy.jpg" title="" /></a>

	<p>October 25, 2017</p>

	<p>LIGHTBULB MOMENT</p>

	<p><a href="https://www.architecturaldigest.com/story/book-cloth-is-secretly-amazing-for-home-decor">That Fabric on Hardcover Books Is Secretly Amazing for Home Decor</a></p>
	</li>
	<li>
	<p>&nbsp;</p>
	<a href="https://www.architecturaldigest.com/story/dimming-switches-overhead-lighting-fix" tabindex="-1"><img alt="Turn Your Horrible Overhead Lighting Into a Perfect Glow" src="https://media.architecturaldigest.com/photos/59ea408261c6482fab68ebb3/16:9/w_768/dimmer-switches.gif" title="" /></a>

	<p>October 20, 2017</p>

	<p>LIGHTING, CAMERA, ACTION</p>

	<p><a href="https://www.architecturaldigest.com/story/dimming-switches-overhead-lighting-fix">Turn Your Horrible Overhead Lighting Into a Perfect Glow</a></p>
	</li>
</ul>
"""
    },
    {
    "title":"home decor ideas",
    "text":"""<h1>22 creative wall d&eacute;cor ideas for Indian homes</h1>

<p><a href="https://www.homify.in/professionals/901483/sunita-vellapally"><img alt="Sunita Vellapally" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_136,q_auto,w_136/v1537182761/p/user/avatar/901483/profile_pic.jpg" />SUNITA VELLAPALLY</a>18 February, 2018</p>

<p><img alt=" Living room by Concept Eight Architects" src="https://images.homify.com/c_fill,f_auto,h_500,q_auto,w_1280/v1442387038/p/photo/image/911164/20140812_ashleyrd_0563.jpg" style="height:500px; width:1280px" /></p>

<p>In the process of finding the perfect furniture and furnishings&nbsp;to decorate the house, often the&nbsp;<a href="https://www.homify.in/rooms/walls-style-modern">walls</a>&nbsp;are neglected. However, it is a feature that can greatly enhance the style of a house and add lots of personality to any room. Decorating the blank walls in your house does not have to be an expensive proposition. In today&rsquo;s ideabook, we bring you 22 creative wall d&eacute;cor ideas, which include cheap D-I-Y solutions, to bring life to boring walls.</p>

<h2>1. Wall of memories</h2>

<p><a href="https://www.homify.in/photo/110699/old-meets-new?collection_id=4911552&amp;collection_type=idea_book&amp;photo_type=photo"><img alt=" Corridor &amp; hallway by The Orange Lane" src="https://images.homify.com/c_fill,f_auto,q_auto,w_488/v1437718077/p/photo/image/110699/7.jpg" style="height:690px; width:488px" /></a></p>

<p><a href="https://www.homify.in/professionals/10133/the-orange-lane"><img alt="The Orange Lane" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_36,q_auto,w_36/v1441789746/p/user/avatar/10133/9_2.jpg" /></a></p>

<h4>Old meets New</h4>

<p><a href="https://www.homify.in/professionals/10133/the-orange-lane">THE ORANGE LANE</a></p>

<p>A blank wall in the passageway or along the staircase can&nbsp;become interesting with the addition of some beautiful family pictures in simple frames. Browse through your collection of photographs or your favourite moments &ndash; vacations, special occasions or life events &ndash; and display them to create unique wall d&eacute;cor in your house.</p>

<h2>2. Wallpaper</h2>

<p><a href="https://www.homify.in/photo/117818/ego-cid-rhythym-hues?collection_id=4911552&amp;collection_type=idea_book&amp;photo_type=photo"><img alt="Ego CID Rhythym, Hues:  Walls &amp; flooring by FurnishTurf" src="https://images.homify.com/c_fill,f_auto,q_auto,w_740/v1437755268/p/photo/image/117818/rc3746room.162e30c5bb.999x800x800.jpg" style="height:740px; width:740px" /></a></p>

<p><a href="https://www.homify.in/professionals/13873/furnishturf"><img alt="FurnishTurf" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_36,q_auto,w_36/v1441791973/p/user/avatar/13873/ft2.jpg" /></a></p>

<h4>Ego CID Rhythym, Hues</h4>

<p><a href="https://www.homify.in/professionals/13873/furnishturf">FURNISHTURF</a>REQUEST QUOTE</p>

<p>Wallpaper is perhaps the most common among living room wall d&eacute;cor ideas. It works&nbsp;irrespective of the size of the house and can add style to even the tiniest apartment. It&rsquo;s easy to install and can be replaced when you want a change.</p>

<p><a href="https://www.homify.in/professionals/5745205/future-space-interior">Ad</a></p>

<p><a href="https://www.homify.in/professionals/5745205/future-space-interior"><img src="https://images.homify.com/image/upload/a_0,c_crop,h_497,w_497,x_71/w_272,h_272,q_auto/v1534408751/p/user/avatar/5745205/FS12.jpg" /></a></p>

<p><a href="https://www.homify.in/professionals/5745205/future-space-interior">Future Space Interior</a></p>

<p><a href="https://www.homify.in/professionals/5745205/future-space-interior">Interior Designers &amp; Decorators</a></p>

<p><a href="https://www.homify.in/professionals/5745205/future-space-interior">Ahmedabad</a></p>

<p><a href="https://www.homify.in/professionals/5745205/future-space-interior"><img alt="Interiors:  Bedroom by Future Space Interior" src="https://images.homify.com/c_fill,f_auto,h_200,q_auto,w_350/v1534408524/p/photo/image/2678777/FS12.jpg" style="height:200px; width:350px" /></a></p>

<p>SHOW PROFILE</p>

<p><a href="https://www.homify.in/professionals/9289/interio-grafiek">Ad</a></p>

<p><a href="https://www.homify.in/professionals/9289/interio-grafiek"><img src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_272,q_auto,w_272/v1482927900/p/user/avatar/9289/IMG_1969.jpg" /></a></p>

<p><a href="https://www.homify.in/professionals/9289/interio-grafiek">Interio Grafiek</a></p>

<p><a href="https://www.homify.in/professionals/9289/interio-grafiek">2 reviews</a></p>

<p><a href="https://www.homify.in/professionals/9289/interio-grafiek">Interior Designers &amp; Decorators</a></p>

<p><a href="https://www.homify.in/professionals/9289/interio-grafiek">Telangana</a></p>

<p><a href="https://www.homify.in/professionals/9289/interio-grafiek"><img alt="Display Kitchen. :   by Interio Grafiek" src="https://images.homify.com/c_fill,f_auto,h_200,q_auto,w_350/v1437586281/p/photo/image/77481/DSC01474.jpg" style="height:200px; width:350px" /></a></p>

<p>SHOW PROFILE</p>

<h2>3. A stunning colour</h2>

<p><a href="https://www.homify.in/photo/911164/ashley-road?collection_id=4911552&amp;collection_type=idea_book&amp;photo_type=photo"><img alt=" Living room by Concept Eight Architects" src="https://images.homify.com/c_fill,f_auto,q_auto,w_740/v1442387038/p/photo/image/911164/20140812_ashleyrd_0563.jpg" style="height:532px; width:740px" /></a></p>

<p><a href="https://www.homify.in/professionals/91698/concept-eight-architects"><img alt="Concept Eight Architects" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_36,q_auto,w_36/v1439822115/p/user/avatar/91698/C8_Logo_FINAL.jpg" /></a></p>

<h4>Ashley Road</h4>

<p><a href="https://www.homify.in/professionals/91698/concept-eight-architects">CONCEPT EIGHT ARCHITECTS</a></p>

<p>The simplest among wall&nbsp;design ideas is to paint the walls in a bright colour. Additionally, you can place accessories such as mirrors or photographs with contrast coloured frames to make the space look spectacular.</p>

<p>Find a&nbsp;<a href="https://www.homify.in/professionals/painters">professional</a>&nbsp;to get your walls painted in a beautiful shade.</p>

<h2>4. A gallery</h2>

<p><a href="https://www.homify.in/photo/1056131/espacios-decorados-by-wallart?collection_id=4911552&amp;collection_type=idea_book&amp;photo_type=photo"><img alt=" Walls by CUSTOMS handmade" src="https://images.homify.com/c_fill,f_auto,q_auto,w_740/v1446105963/p/photo/image/1056131/12189997_1123196447699443_7145744895712199278_n.jpg" style="height:493px; width:740px" /></a></p>

<p><a href="https://www.homify.in/professionals/208951/customs-handmade"><img alt="CUSTOMS handmade" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_36,q_auto,w_36/v1487159362/p/user/avatar/208951/Customs-logo.jpg" /></a></p>

<h4>Espacios decorados by Wallart</h4>

<p><a href="https://www.homify.in/professionals/208951/customs-handmade">CUSTOMS HANDMADE</a></p>

<p>Nothing brings life to a wall more than a collection of art&nbsp;or artefacts. Whether it&rsquo;s a collection of posters, photographs, paintings or crockery, this is an idea that works well, especially as large wall d&eacute;cor.</p>

<h2>5. A beautiful landscape</h2>

<p><a href="https://www.homify.in/photo/712372/bedroom-wall-mural?collection_id=4911552&amp;collection_type=idea_book&amp;photo_type=photo"><img alt=" Artwork by Transform a Wall" src="https://images.homify.com/c_fill,f_auto,q_auto,w_740/v1441107532/p/photo/image/712372/bedroom_camera_pink_blossom.jpg" style="height:518px; width:740px" /></a></p>

<p><a href="https://www.homify.in/professionals/78989/transform-a-wall"><img alt="Transform a Wall" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_36,q_auto,w_36/v1441847290/p/user/avatar/78989/1435764058-logo-transformawall-green.jpg" /></a></p>

<h4>Bedroom wall mural</h4>

<p><a href="https://www.homify.in/professionals/78989/transform-a-wall">TRANSFORM A WALL</a></p>

<p>Bedrooms need to be soothing so that it allows you to relax&nbsp;within. Among the best wall d&eacute;cor ideas for bedrooms is installing a wallpaper with a beautiful scenery to create a calm ambiance in the room. It can work just as well in&nbsp;<a href="https://www.homify.in/rooms/living-room-style-minimalist">living rooms&nbsp;</a>or dining areas.</p>

<h2>6. A carpet or tapestry</h2>

<p><a href="https://www.homify.in/photo/318850/mandela-moon?collection_id=4911552&amp;collection_type=idea_book&amp;photo_type=photo"><img alt=" Walls &amp; flooring by Wendy Morrison" src="https://images.homify.com/c_fill,f_auto,q_auto,w_488/v1438420176/p/photo/image/318850/Wendy_Morrison_Mandela_Moon_-_wall.jpg" style="height:732px; width:488px" /></a></p>

<p><a href="https://www.homify.in/professionals/25100/wendy-morrison"><img alt="Wendy Morrison" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_36,q_auto,w_36/v1441799453/p/user/avatar/25100/Wendy_Morrison_logo.jpg" /></a></p>

<h4>Mandela Moon</h4>

<p><a href="https://www.homify.in/professionals/25100/wendy-morrison">WENDY MORRISON</a></p>

<p>Before you throw out an unused rug or tapestry, look around&nbsp;your home and see whether it can add beauty to one of the walls. Hanging old rugs on the wall is a cheap wall d&eacute;cor idea as you the only things you need to spend on are a few nails and a frame to mount it on the wall.</p>

<p>&nbsp;</p>

<p><a href="https://www.homify.in/free-consultation?from=ideabook_1"><img alt=" Houses by Casas inHAUS" src="https://images.homify.com/c_fill,f_auto,h_340,q_auto,w_1700/v1449165691/p/photo/image/1173452/Modelo_Chipiona_exterior.jpg" style="height:340px; width:1700px" /></a></p>

<p><br />
<a href="https://www.homify.in/free-consultation?from=ideabook_1"><strong>Need help with your home project? We&#39;ll help you find the right professional</strong></a></p>

<p>REQUEST FREE CONSULTATION</p>

<h2>7. Hand painted images</h2>

<p><a href="https://www.homify.in/photo/202576/wandsticker-friedegunde-co?collection_id=4911552&amp;collection_type=idea_book&amp;photo_type=photo"><img alt=" Walls &amp; flooring by cats on appletrees" src="https://images.homify.com/c_fill,f_auto,q_auto,w_740/v1438303769/p/photo/image/202576/Wandsticker-U_bersicht.jpg" style="height:479px; width:740px" /></a></p>

<p><a href="https://www.homify.in/professionals/24743/cats-on-appletrees"><img alt="cats on appletrees" src="https://images.homify.com/image/upload/a_0,c_fill,f_auto,h_36,q_auto,w_36/v1441799111/p/user/avatar/24743/Unbenannt.jpg" /></a></p>

<h4>&nbsp;</h4>

<p><a href="https://www.homify.in/professionals/24743/cats-on-appletrees">CATS ON APPLETREES</a></p>

<p>For kids&rsquo; bedrooms&nbsp;among the cheap wall d&eacute;cor ideas, DIY solutions such as hand painted motifs or&nbsp;stencils&nbsp;of cartoon characters or animals are a great idea for adding a fun touch to the space.</p>

<p>Get more&nbsp;<a href="https://www.homify.in/ideabooks/232061/6-affordable-tips-for-wall-decor">ideas for affordable wall decor</a>.</p>

<h2>8. Texture</h2>
 """

    },
    {
    "title":" top engineering colleges in india ",
    "text":""" <h1>Top Engineering Colleges in India 2019</h1>

<p>Get rankings, placement reviews, fees&nbsp;and Q&amp;A related to admission, cut-off and eligibility of Top Engineering Colleges. The rankings are published by NIRF/MHRD, India Today, The Week, Times and Outlook. Also see rankings for:</p>

<p><a href="https://www.shiksha.com/b-tech/ranking/top-computer-science-engineering-colleges-in-india/46-2-0-0-0?utm_source=rp_india&amp;utm_medium=btech&amp;utm_campaign=bhst_link">Top Computer Science Engineering Colleges</a>&nbsp;&nbsp;<a href="https://www.shiksha.com/b-tech/ranking/top-aeronautical-engineering-colleges-in-india/49-2-0-0-0?utm_source=rp_india&amp;utm_medium=btech&amp;utm_campaign=bhst_link">Top Aeronautical Engineering Colleges</a></p>

<p><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india-accepting-jee-main/44-2-0-0-6244?utm_source=rp_india&amp;utm_medium=btech&amp;utm_campaign=bhst_link">Top Engineering Colleges accepting JEE Main</a>&nbsp;&nbsp;<a href="https://www.shiksha.com/engineering/ranking/top-private-engineering-colleges-in-india/109-2-0-0-0?utm_source=rp_india&amp;utm_medium=btech&amp;utm_campaign=bhst_link">Top Private Engineering Colleges in India</a></p>

<p>&nbsp;<a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-karnataka/44-2-106-0-0?utm_source=rp_india&amp;utm_medium=btech&amp;utm_campaign=bhst_link">Top Engineering Colleges in Karnataka</a>&nbsp;&nbsp;<a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-maharashtra/44-2-114-0-0?utm_source=rp_india&amp;utm_medium=btech&amp;utm_campaign=bhst_link">Top Engineering Colleges in Maharastra</a></p>

<p><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-kerala/44-2-107-0-0?utm_source=rp_india&amp;utm_medium=btech&amp;utm_campaign=bhst_link">Top Engineering Colleges in Kerela</a></p>

<p>Filters :</p>

<p>Ranked by</p>

<p>All Publishers&nbsp;(291)</p>

<p>Specialization</p>

<p>Engineering</p>

<p>Location</p>

<p>All Location</p>

<p>Exam</p>

<p>All Exam</p>

<p>&nbsp;</p>

<p>NIRF</p>

<p>1</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>4</p>

<p><img alt="IIT Madras - Indian Institute of Technology Chennai (IITM)" src="https://images.shiksha.com/mediadata/images/1488170835phpYHm6bs_100x78.jpg" style="height:78px; width:100px" title="IIT Madras - Indian Institute of Technology Chennai (IITM)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-chennai-iitm-adyar-3031" title="IIT Madras - Indian Institute of Technology Chennai (IITM)">IIT Madras - Indian Institute of Technology Chennai (IITM)</a></h4>

<p>Chennai<a href="https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-chennai-iitm-adyar-3031/admission">Admissions 2019</a></p>

<p>4.6<a href="https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-chennai-iitm-adyar-3031/reviews">(94)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-chennai-iitm-adyar-3031/courses">59&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>2</p>

<p>India Today</p>

<p>1</p>

<p>The Week</p>

<p>1</p>

<p><img alt="IIT Delhi - Indian Institute of Technology (IITD)" src="https://images.shiksha.com/mediadata/images/1504610950phpzuhaTW_100x78.jpg" style="height:78px; width:100px" title="IIT Delhi - Indian Institute of Technology (IITD)" /></p>

<h4><a href="https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-iitd-53938" title="IIT Delhi - Indian Institute of Technology (IITD)">IIT Delhi - Indian Institute of Technology (IITD)</a></h4>

<p>Delhi<a href="https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-iitd-53938/admission">Admissions 2019</a></p>

<p>4.4<a href="https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-iitd-53938/reviews">(173)</a></p>

<p>|<a href="https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-iitd-53938/courses">69&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>3</p>

<p>India Today</p>

<p>3</p>

<p>The Week</p>

<p>2</p>

<p><img alt="IIT Bombay - Indian Institute of Technology (IITB)" src="https://images.shiksha.com/mediadata/images/1507098026phpzkXsFb_100x78.jpg" style="height:78px; width:100px" title="IIT Bombay - Indian Institute of Technology (IITB)" /></p>

<h4><a href="https://www.shiksha.com/university/iit-bombay-indian-institute-of-technology-iitb-mumbai-54212" title="IIT Bombay - Indian Institute of Technology (IITB)">IIT Bombay - Indian Institute of Technology (IITB)</a></h4>

<p>Mumbai<a href="https://www.shiksha.com/university/iit-bombay-indian-institute-of-technology-iitb-mumbai-54212/admission">Admissions 2019</a></p>

<p>4.7<a href="https://www.shiksha.com/university/iit-bombay-indian-institute-of-technology-iitb-mumbai-54212/reviews">(176)</a></p>

<p>|<a href="https://www.shiksha.com/university/iit-bombay-indian-institute-of-technology-iitb-mumbai-54212/courses">64&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>&nbsp;</p>

<p>NIRF</p>

<p>4</p>

<p>India Today</p>

<p>2</p>

<p>The Week</p>

<p>3</p>

<p><img alt="IIT Kharagpur - Indian Institute of Technology (IITKGP)" src="https://images.shiksha.com/mediadata/images/1549359594phpvIFLi0_100x78.png" style="height:78px; width:100px" title="IIT Kharagpur - Indian Institute of Technology (IITKGP)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-kharagpur-indian-institute-of-technology-iitkgp-2999" title="IIT Kharagpur - Indian Institute of Technology (IITKGP)">IIT Kharagpur - Indian Institute of Technology (IITKGP)</a></h4>

<p>Kharagpur<a href="https://www.shiksha.com/college/iit-kharagpur-indian-institute-of-technology-iitkgp-2999/admission">Admissions 2019</a></p>

<p>4.5<a href="https://www.shiksha.com/college/iit-kharagpur-indian-institute-of-technology-iitkgp-2999/reviews">(217)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-kharagpur-indian-institute-of-technology-iitkgp-2999/courses">146&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<h2>Get college recommendation based on the engineering exams you have given</h2>

<p><a href="https://www.shiksha.com/college-predictor">Get Recommendations Now</a></p>

<p>NIRF</p>

<p>5</p>

<p>India Today</p>

<p>4</p>

<p>The Week</p>

<p>5</p>

<p><img alt="IIT Kanpur - Indian Institute of Technology (IITK)" src="https://images.shiksha.com/mediadata/images/1504590879phpMwnfk8_100x78.jpg" style="height:78px; width:100px" title="IIT Kanpur - Indian Institute of Technology (IITK)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-kanpur-indian-institute-of-technology-iitk-25116" title="IIT Kanpur - Indian Institute of Technology (IITK)">IIT Kanpur - Indian Institute of Technology (IITK)</a></h4>

<p>Kanpur<a href="https://www.shiksha.com/college/iit-kanpur-indian-institute-of-technology-iitk-25116/admission">Admissions 2019</a></p>

<p>4.7<a href="https://www.shiksha.com/college/iit-kanpur-indian-institute-of-technology-iitk-25116/reviews">(105)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-kanpur-indian-institute-of-technology-iitk-25116/courses">62&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>6</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>6</p>

<p><img alt="IIT Roorkee - Indian Institute of Technology (IITR)" src="https://images.shiksha.com/mediadata/images/1488178566phpKszqm5_100x78.jpg" style="height:78px; width:100px" title="IIT Roorkee - Indian Institute of Technology (IITR)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-roorkee-indian-institute-of-technology-iitr-3057" title="IIT Roorkee - Indian Institute of Technology (IITR)">IIT Roorkee - Indian Institute of Technology (IITR)</a></h4>

<p>Roorkee<a href="https://www.shiksha.com/college/iit-roorkee-indian-institute-of-technology-iitr-3057/admission">Admissions 2019</a></p>

<p>4.4<a href="https://www.shiksha.com/college/iit-roorkee-indian-institute-of-technology-iitr-3057/reviews">(200)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-roorkee-indian-institute-of-technology-iitr-3057/courses">73&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>7</p>

<p>India Today</p>

<p>6</p>

<p>The Week</p>

<p>7</p>

<p><img alt="IIT Guwahati - Indian Institute of Technology (IITG)" src="https://images.shiksha.com/mediadata/images/1557308060phpUCn7yA_100x78.jpg" style="height:78px; width:100px" title="IIT Guwahati - Indian Institute of Technology (IITG)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-guwahati-indian-institute-of-technology-iitg-3065" title="IIT Guwahati - Indian Institute of Technology (IITG)">IIT Guwahati - Indian Institute of Technology (IITG)</a></h4>

<p>Guwahati<a href="https://www.shiksha.com/college/iit-guwahati-indian-institute-of-technology-iitg-3065/admission">Admissions 2019</a></p>

<p>4.4<a href="https://www.shiksha.com/college/iit-guwahati-indian-institute-of-technology-iitg-3065/reviews">(104)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-guwahati-indian-institute-of-technology-iitg-3065/courses">27&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>9</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>11</p>

<p><img alt="CEG - College of Engineering Guindy" src="https://images.shiksha.com/mediadata/images/1547804056phpGT8DhX_100x78.jpg" style="height:78px; width:100px" title="CEG - College of Engineering Guindy" /></p>

<h4><a href="https://www.shiksha.com/college/ceg-college-of-engineering-guindy-guindy-chennai-51546" title="CEG - College of Engineering Guindy">CEG - College of Engineering Guindy</a></h4>

<p>Chennai</p>

<p>4.4<a href="https://www.shiksha.com/college/ceg-college-of-engineering-guindy-guindy-chennai-51546/reviews">(88)</a></p>

<p>|<a href="https://www.shiksha.com/college/ceg-college-of-engineering-guindy-guindy-chennai-51546/courses">96&nbsp;Courses</a></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>8</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="IIT Hyderabad - Indian Institute of Technology (IITH)" src="https://images.shiksha.com/mediadata/images/1488179661phpkvuxWQ_100x78.jpg" style="height:78px; width:100px" title="IIT Hyderabad - Indian Institute of Technology (IITH)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-hyderabad-indian-institute-of-technology-iith-32726" title="IIT Hyderabad - Indian Institute of Technology (IITH)">IIT Hyderabad - Indian Institute of Technology (IITH)</a></h4>

<p>Hyderabad<a href="https://www.shiksha.com/college/iit-hyderabad-indian-institute-of-technology-iith-32726/admission">Admissions 2019</a></p>

<p>4.6<a href="https://www.shiksha.com/college/iit-hyderabad-indian-institute-of-technology-iith-32726/reviews">(26)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-hyderabad-indian-institute-of-technology-iith-32726/courses">27&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>25</p>

<p>India Today</p>

<p>7</p>

<p>The Week</p>

<p>8</p>

<p><img alt="BITS Pilani - Birla Institute of Technology and Science" src="https://images.shiksha.com/mediadata/images/1527846035phpLHddHX_100x78.png" style="height:78px; width:100px" title="BITS Pilani - Birla Institute of Technology and Science" /></p>

<h4><a href="https://www.shiksha.com/university/bits-pilani-birla-institute-of-technology-and-science-467" title="BITS Pilani - Birla Institute of Technology and Science">BITS Pilani - Birla Institute of Technology and Science</a></h4>

<p>Pilani<a href="https://www.shiksha.com/university/bits-pilani-birla-institute-of-technology-and-science-467/admission">Admissions 2019</a></p>

<p>4.3<a href="https://www.shiksha.com/university/bits-pilani-birla-institute-of-technology-and-science-467/reviews">(360)</a></p>

<p>|<a href="https://www.shiksha.com/university/bits-pilani-birla-institute-of-technology-and-science-467/courses">107&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/bitsat-exam">BITSAT</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>10</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>12</p>

<p><img alt="NIT Trichy - National Institute of Technology, Tiruchirappalli (NITT)" src="https://images.shiksha.com/mediadata/images/1551065772php61xxGi_100x78.jpg" style="height:78px; width:100px" title="NIT Trichy - National Institute of Technology, Tiruchirappalli (NITT)" /></p>

<h4><a href="https://www.shiksha.com/university/nit-trichy-national-institute-of-technology-tiruchirappalli-nitt-2996" title="NIT Trichy - National Institute of Technology, Tiruchirappalli (NITT)">NIT Trichy - National Institute of Technology, Tiruchirappalli (NITT)</a></h4>

<p>Tiruchirappalli<a href="https://www.shiksha.com/university/nit-trichy-national-institute-of-technology-tiruchirappalli-nitt-2996/admission">Admissions 2019</a></p>

<p>4.3<a href="https://www.shiksha.com/university/nit-trichy-national-institute-of-technology-tiruchirappalli-nitt-2996/reviews">(174)</a></p>

<p>|<a href="https://www.shiksha.com/university/nit-trichy-national-institute-of-technology-tiruchirappalli-nitt-2996/courses">50&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>12</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="ICT Mumbai - Institute of Chemical Technology (UDCT)" src="https://images.shiksha.com/mediadata/images/1531794464php2Ge9pt_100x78.jpg" style="height:78px; width:100px" title="ICT Mumbai - Institute of Chemical Technology (UDCT)" /></p>

<h4><a href="https://www.shiksha.com/university/ict-mumbai-institute-of-chemical-technology-udct-36791" title="ICT Mumbai - Institute of Chemical Technology (UDCT)">ICT Mumbai - Institute of Chemical Technology (UDCT)</a></h4>

<p>Mumbai<a href="https://www.shiksha.com/university/ict-mumbai-institute-of-chemical-technology-udct-36791/admission">Admissions 2019</a></p>

<p>4.4<a href="https://www.shiksha.com/university/ict-mumbai-institute-of-chemical-technology-udct-36791/reviews">(33)</a></p>

<p>|<a href="https://www.shiksha.com/university/ict-mumbai-institute-of-chemical-technology-udct-36791/courses">16&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a>,<a href="https://www.shiksha.com/b-tech/mht-cet-exam">MHT CET</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>Not Ranked</p>

<p>India Today</p>

<p>9</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="IIT (ISM) Dhanbad - Indian Institute of Technology (Indian School of Mines)" src="https://images.shiksha.com/mediadata/images/1504507062phprv118w_100x78.jpg" style="height:78px; width:100px" title="IIT (ISM) Dhanbad - Indian Institute of Technology (Indian School of Mines)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-ism-dhanbad-indian-institute-of-technology-indian-school-of-mines-13669" title="IIT (ISM) Dhanbad - Indian Institute of Technology (Indian School of Mines)">IIT (ISM) Dhanbad - Indian Institute of Technology (Indian School of Mines)</a></h4>

<p>Dhanbad<a href="https://www.shiksha.com/college/iit-ism-dhanbad-indian-institute-of-technology-indian-school-of-mines-13669/admission">Admissions 2019</a></p>

<p>4.1<a href="https://www.shiksha.com/college/iit-ism-dhanbad-indian-institute-of-technology-indian-school-of-mines-13669/reviews">(212)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-ism-dhanbad-indian-institute-of-technology-indian-school-of-mines-13669/courses">59&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>15</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>15</p>

<p><img alt="IIT Dhanbad (Indian School of Mines) - Department of Petroleum Engineering" src="https://images.shiksha.com/mediadata/images/1506424861phpIMG7q4_100x78.jpg" style="height:78px; width:100px" title="IIT Dhanbad (Indian School of Mines) - Department of Petroleum Engineering" /></p>

<h4><a href="https://www.shiksha.com/college/iit-dhanbad-indian-school-of-mines-department-of-petroleum-engineering-54154" title="IIT Dhanbad (Indian School of Mines) - Department of Petroleum Engineering">IIT Dhanbad (Indian School of Mines) - Department of Petroleum Engineering</a></h4>

<p>Dhanbad</p>

<p>4.2<a href="https://www.shiksha.com/college/iit-dhanbad-indian-school-of-mines-department-of-petroleum-engineering-54154/reviews">(22)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-dhanbad-indian-school-of-mines-department-of-petroleum-engineering-54154/courses">2&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>14</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>20</p>

<p><img alt="Jadavpur University" src="https://images.shiksha.com/mediadata/images/1531632262php3PNz6z_100x78.png" style="height:78px; width:100px" title="Jadavpur University" /></p>

<h4><a href="https://www.shiksha.com/university/jadavpur-university-kolkata-19992" title="Jadavpur University">Jadavpur University</a></h4>

<p>Kolkata<a href="https://www.shiksha.com/university/jadavpur-university-kolkata-19992/admission">Admissions 2019</a></p>

<p>4.4<a href="https://www.shiksha.com/university/jadavpur-university-kolkata-19992/reviews">(265)</a></p>

<p>|<a href="https://www.shiksha.com/university/jadavpur-university-kolkata-19992/courses">81&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/wbjee-exam">WBJEE</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>13</p>

<p>India Today</p>

<p>10</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="IIT Indore - Indian Institute of Technology, Indore (IITI)" src="https://images.shiksha.com/mediadata/images/1488192881phpR8rY1q_100x78.jpg" style="height:78px; width:100px" title="IIT Indore - Indian Institute of Technology, Indore (IITI)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-indore-indian-institute-of-technology-indore-iiti-38240" title="IIT Indore - Indian Institute of Technology, Indore (IITI)">IIT Indore - Indian Institute of Technology, Indore (IITI)</a></h4>

<p>Indore<a href="https://www.shiksha.com/college/iit-indore-indian-institute-of-technology-indore-iiti-38240/admission">Admissions 2019</a></p>

<p>4.0<a href="https://www.shiksha.com/college/iit-indore-indian-institute-of-technology-indore-iiti-38240/reviews">(15)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-indore-indian-institute-of-technology-indore-iiti-38240/courses">14&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>18</p>

<p>India Today</p>

<p>20</p>

<p>The Week</p>

<p>22</p>

<p><img alt="VIT University - Vellore Institute of Technology" src="https://images.shiksha.com/mediadata/images/1488188893phpaxZqAB_100x78.jpg" style="height:78px; width:100px" title="VIT University - Vellore Institute of Technology" /></p>

<h4><a href="https://www.shiksha.com/university/vit-university-vellore-institute-of-technology-29714" title="VIT University - Vellore Institute of Technology">VIT University - Vellore Institute of Technology</a></h4>

<p>Vellore<a href="https://www.shiksha.com/university/vit-university-vellore-institute-of-technology-29714/admission">Admissions 2019</a></p>

<p>4.2<a href="https://www.shiksha.com/university/vit-university-vellore-institute-of-technology-29714/reviews">(890)</a></p>

<p>|<a href="https://www.shiksha.com/university/vit-university-vellore-institute-of-technology-29714/courses">67&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/viteee-exam">VITEEE</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>16</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>16</p>

<p><img alt="NIT Rourkela - National Institute of Technology (NITRKL)" src="https://images.shiksha.com/mediadata/images/1488266598php3R71Eb_100x78.jpg" style="height:78px; width:100px" title="NIT Rourkela - National Institute of Technology (NITRKL)" /></p>

<h4><a href="https://www.shiksha.com/university/nit-rourkela-national-institute-of-technology-nitrkl-28530" title="NIT Rourkela - National Institute of Technology (NITRKL)">NIT Rourkela - National Institute of Technology (NITRKL)</a></h4>

<p>Rourkela<a href="https://www.shiksha.com/university/nit-rourkela-national-institute-of-technology-nitrkl-28530/admission">Admissions 2019</a></p>

<p>4.2<a href="https://www.shiksha.com/university/nit-rourkela-national-institute-of-technology-nitrkl-28530/reviews">(202)</a></p>

<p>|<a href="https://www.shiksha.com/university/nit-rourkela-national-institute-of-technology-nitrkl-28530/courses">57&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>17</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>26</p>

<p><img alt="IIT Bhubaneswar - Indian Institute of Technology Bhubaneswar" src="https://images.shiksha.ws/public/images/instDefault_210x157.png" style="height:78px; width:100px" title="IIT Bhubaneswar - Indian Institute of Technology Bhubaneswar" /></p>

<h4><a href="https://www.shiksha.com/college/iit-bhubaneswar-indian-institute-of-technology-bhubaneswar-32717" title="IIT Bhubaneswar - Indian Institute of Technology Bhubaneswar">IIT Bhubaneswar - Indian Institute of Technology Bhubaneswar</a></h4>

<p>Bhubaneswar<a href="https://www.shiksha.com/college/iit-bhubaneswar-indian-institute-of-technology-bhubaneswar-32717/admission">Admissions 2019</a></p>

<p>4.2<a href="https://www.shiksha.com/college/iit-bhubaneswar-indian-institute-of-technology-bhubaneswar-32717/reviews">(27)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-bhubaneswar-indian-institute-of-technology-bhubaneswar-32717/courses">16&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>Not Ranked</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>21</p>

<p><img alt="NSIT - Netaji Subhas University of Technology" src="https://images.shiksha.com/mediadata/images/1551151713phpS45Q6A_100x78.jpg" style="height:78px; width:100px" title="NSIT - Netaji Subhas University of Technology" /></p>

<h4><a href="https://www.shiksha.com/college/nsit-netaji-subhas-university-of-technology-dwarka-delhi-28573" title="NSIT - Netaji Subhas University of Technology">NSIT - Netaji Subhas University of Technology</a></h4>

<p>Delhi<a href="https://www.shiksha.com/college/nsit-netaji-subhas-university-of-technology-dwarka-delhi-28573/admission">Admissions 2019</a></p>

<p>4.0<a href="https://www.shiksha.com/college/nsit-netaji-subhas-university-of-technology-dwarka-delhi-28573/reviews">(171)</a></p>

<p>|<a href="https://www.shiksha.com/college/nsit-netaji-subhas-university-of-technology-dwarka-delhi-28573/courses">17&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a>,<a href="javascript:void(0);">SAT</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>Not Ranked</p>

<p>India Today</p>

<p>17</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="NIT Surathkal (NITK) - National Institute of Technology" src="https://images.shiksha.com/mediadata/images/1550643698phpAmIN2k_100x78.png" style="height:78px; width:100px" title="NIT Surathkal (NITK) - National Institute of Technology" /></p>

<h4><a href="https://www.shiksha.com/college/nit-surathkal-nitk-national-institute-of-technology-mangalore-24187" title="NIT Surathkal (NITK) - National Institute of Technology">NIT Surathkal (NITK) - National Institute of Technology</a></h4>

<p>Mangalore<a href="https://www.shiksha.com/college/nit-surathkal-nitk-national-institute-of-technology-mangalore-24187/admission">Admissions 2019</a></p>

<p>4.3<a href="https://www.shiksha.com/college/nit-surathkal-nitk-national-institute-of-technology-mangalore-24187/reviews">(198)</a></p>

<p>|<a href="https://www.shiksha.com/college/nit-surathkal-nitk-national-institute-of-technology-mangalore-24187/courses">52&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>33</p>

<p>India Today</p>

<p>15</p>

<p>The Week</p>

<p>18</p>

<p><img alt="BIT Mesra - Birla Institute of Technology" src="https://images.shiksha.com/mediadata/images/1556693335phplrvNBp_100x78.jpg" style="height:78px; width:100px" title="BIT Mesra - Birla Institute of Technology" /></p>

<h4><a href="https://www.shiksha.com/university/bit-mesra-birla-institute-of-technology-ranchi-24087" title="BIT Mesra - Birla Institute of Technology">BIT Mesra - Birla Institute of Technology</a></h4>

<p>Ranchi<a href="https://www.shiksha.com/university/bit-mesra-birla-institute-of-technology-ranchi-24087/admission">Admissions 2019</a></p>

<p>3.9<a href="https://www.shiksha.com/university/bit-mesra-birla-institute-of-technology-ranchi-24087/reviews">(350)</a></p>

<p>|<a href="https://www.shiksha.com/university/bit-mesra-birla-institute-of-technology-ranchi-24087/courses">59&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>29</p>

<p>India Today</p>

<p>12</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="IIT Ropar - Indian Institute of Technology, Ropar (IIT-RPR)" src="https://images.shiksha.com/mediadata/images/1488180341phpRnPodM_100x78.jpg" style="height:78px; width:100px" title="IIT Ropar - Indian Institute of Technology, Ropar (IIT-RPR)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-ropar-indian-institute-of-technology-ropar-iit-rpr-32693" title="IIT Ropar - Indian Institute of Technology, Ropar (IIT-RPR)">IIT Ropar - Indian Institute of Technology, Ropar (IIT-RPR)</a></h4>

<p>Ropar<a href="https://www.shiksha.com/college/iit-ropar-indian-institute-of-technology-ropar-iit-rpr-32693/admission">Admissions 2019</a></p>

<p>4.4<a href="https://www.shiksha.com/college/iit-ropar-indian-institute-of-technology-ropar-iit-rpr-32693/reviews">(23)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-ropar-indian-institute-of-technology-ropar-iit-rpr-32693/courses">25&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>23</p>

<p>India Today</p>

<p>22</p>

<p>The Week</p>

<p>30</p>

<p><img alt="Thapar Institute of Engineering and Technology" src="https://images.shiksha.com/mediadata/images/1553593636phpZ7AI08_100x78.jpg" style="height:78px; width:100px" title="Thapar Institute of Engineering and Technology" /></p>

<h4><a href="https://www.shiksha.com/university/thapar-institute-of-engineering-and-technology-patiala-3015" title="Thapar Institute of Engineering and Technology">Thapar Institute of Engineering and Technology</a></h4>

<p>Patiala<a href="https://www.shiksha.com/university/thapar-institute-of-engineering-and-technology-patiala-3015/admission">Admissions 2019</a></p>

<p>4.0<a href="https://www.shiksha.com/university/thapar-institute-of-engineering-and-technology-patiala-3015/reviews">(384)</a></p>

<p>|<a href="https://www.shiksha.com/university/thapar-institute-of-engineering-and-technology-patiala-3015/courses">60&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>24</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="IIT Gandhinagar - Indian Institute of Technology (IITGN)" src="https://images.shiksha.com/mediadata/images/1488194901phpQ6pinf_100x78.jpg" style="height:78px; width:100px" title="IIT Gandhinagar - Indian Institute of Technology (IITGN)" /></p>

<h4><a href="https://www.shiksha.com/college/iit-gandhinagar-indian-institute-of-technology-iitgn-32705" title="IIT Gandhinagar - Indian Institute of Technology (IITGN)">IIT Gandhinagar - Indian Institute of Technology (IITGN)</a></h4>

<p>Gandhinagar<a href="https://www.shiksha.com/college/iit-gandhinagar-indian-institute-of-technology-iitgn-32705/admission">Admissions 2019</a></p>

<p>4.4<a href="https://www.shiksha.com/college/iit-gandhinagar-indian-institute-of-technology-iitgn-32705/reviews">(15)</a></p>

<p>|<a href="https://www.shiksha.com/college/iit-gandhinagar-indian-institute-of-technology-iitgn-32705/courses">25&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>30</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="IIST - Indian Institute of Space Science and Technology" src="https://images.shiksha.com/mediadata/images/1533034061phphrCmUt_100x78.png" style="height:78px; width:100px" title="IIST - Indian Institute of Space Science and Technology" /></p>

<h4><a href="https://www.shiksha.com/university/iist-indian-institute-of-space-science-and-technology-thiruvananthapuram-25141" title="IIST - Indian Institute of Space Science and Technology">IIST - Indian Institute of Space Science and Technology</a></h4>

<p>Thiruvananthapuram<a href="https://www.shiksha.com/university/iist-indian-institute-of-space-science-and-technology-thiruvananthapuram-25141/admission">Admissions 2019</a></p>

<p>3.9<a href="https://www.shiksha.com/university/iist-indian-institute-of-space-science-and-technology-thiruvananthapuram-25141/reviews">(17)</a></p>

<p>|<a href="https://www.shiksha.com/university/iist-indian-institute-of-space-science-and-technology-thiruvananthapuram-25141/courses">5&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-advanced-exam">JEE Advanced</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>Not Ranked</p>

<p>India Today</p>

<p>29</p>

<p>The Week</p>

<p>Not Ranked</p>

<p><img alt="SIT - Symbiosis Institute of Technology" src="https://images.shiksha.com/mediadata/images/1489222981phpSAZtlF_100x78.jpg" style="height:78px; width:100px" title="SIT - Symbiosis Institute of Technology" /></p>

<h4><a href="https://www.shiksha.com/college/sit-symbiosis-institute-of-technology-lavale-village-pune-29564" title="SIT - Symbiosis Institute of Technology">SIT - Symbiosis Institute of Technology</a></h4>

<p>Pune</p>

<p>3.8<a href="https://www.shiksha.com/college/sit-symbiosis-institute-of-technology-lavale-village-pune-29564/reviews">(49)</a></p>

<p>|<a href="https://www.shiksha.com/college/sit-symbiosis-institute-of-technology-lavale-village-pune-29564/courses">14&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/siteee-exam">SITEEE</a>,<a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a>,<a href="https://www.shiksha.com/b-tech/mht-cet-exam">MHT CET</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>19</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>19</p>

<p><img alt="IIEST Shibpur - Indian Institute of Engineering Science and Technology (BESU Shibpur)" src="https://images.shiksha.com/mediadata/images/1553825246phpOiC5fS_100x78.png" style="height:78px; width:100px" title="IIEST Shibpur - Indian Institute of Engineering Science and Technology (BESU Shibpur)" /></p>

<h4><a href="https://www.shiksha.com/college/iiest-shibpur-indian-institute-of-engineering-science-and-technology-besu-shibpur-howrah-24176" title="IIEST Shibpur - Indian Institute of Engineering Science and Technology (BESU Shibpur)">IIEST Shibpur - Indian Institute of Engineering Science and Technology (BESU Shibpur)</a></h4>

<p>Howrah<a href="https://www.shiksha.com/college/iiest-shibpur-indian-institute-of-engineering-science-and-technology-besu-shibpur-howrah-24176/admission">Admissions 2019</a></p>

<p>4.1<a href="https://www.shiksha.com/college/iiest-shibpur-indian-institute-of-engineering-science-and-technology-besu-shibpur-howrah-24176/reviews">(142)</a></p>

<p>|<a href="https://www.shiksha.com/college/iiest-shibpur-indian-institute-of-engineering-science-and-technology-besu-shibpur-howrah-24176/courses">48&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>26</p>

<p>India Today</p>

<p>Not Ranked</p>

<p>The Week</p>

<p>13</p>

<p><img alt="NIT Warangal (NITW) - National Institute of Technology" src="https://images.shiksha.com/mediadata/images/1488178282php24ZflQ_100x78.jpg" style="height:78px; width:100px" title="NIT Warangal (NITW) - National Institute of Technology" /></p>

<h4><a href="https://www.shiksha.com/college/nit-warangal-nitw-national-institute-of-technology-25425" title="NIT Warangal (NITW) - National Institute of Technology">NIT Warangal (NITW) - National Institute of Technology</a></h4>

<p>Warangal<a href="https://www.shiksha.com/college/nit-warangal-nitw-national-institute-of-technology-25425/admission">Admissions 2019</a></p>

<p>4.2<a href="https://www.shiksha.com/college/nit-warangal-nitw-national-institute-of-technology-25425/reviews">(255)</a></p>

<p>|<a href="https://www.shiksha.com/college/nit-warangal-nitw-national-institute-of-technology-25425/courses">40&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<p>NIRF</p>

<p>34</p>

<p>India Today</p>

<p>8</p>

<p>The Week</p>

<p>10</p>

<h4><a href="https://www.shiksha.com/university/dtu-delhi-technological-university-dce-23920" title="DTU - Delhi Technological University (DCE)">DTU - Delhi Technological University (DCE)</a></h4>

<p>Delhi<a href="https://www.shiksha.com/university/dtu-delhi-technological-university-dce-23920/admission">Admissions 2019</a></p>

<p>4.2<a href="https://www.shiksha.com/university/dtu-delhi-technological-university-dce-23920/reviews">(439)</a></p>

<p>|<a href="https://www.shiksha.com/university/dtu-delhi-technological-university-dce-23920/courses">24&nbsp;Courses</a></p>

<p>Exams<strong><a href="https://www.shiksha.com/b-tech/jee-main-exam">JEE Main</a></strong></p>

<p>ShortlistApply Now</p>

<ul>
	<li>&nbsp;</li>
	<li><a href="javascript:void(0);">1</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0?pageNo=2">2</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0?pageNo=3">3</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0?pageNo=4">4</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0?pageNo=5">5</a></li>
	<li>&nbsp;</li>
</ul>

<p><a href="javascript:void(0);">Show data in table</a></p>

<h2>Top Ranked Engineering Colleges in</h2>

<h4>Cities</h4>

<ul>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-delhi-ncr/44-2-0-10223-0">Delhi / NCR</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-hyderabad/44-2-0-702-0">Hyderabad</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-bangalore/44-2-0-278-0">Bangalore</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-chennai/44-2-0-64-0">Chennai</a></li>
</ul>

<p>View All</p>

<h4>States</h4>

<ul>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0">All Location</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-maharashtra/44-2-114-0-0">Maharashtra</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-karnataka/44-2-106-0-0">Karnataka</a></li>
	<li><a href="https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-uttar-pradesh/44-2-126-0-0">Uttar Pradesh</a></li>
</ul>

<p>View All</p>

<p><a href="javascript:void(0);" id="crossStickyBanner">&times;</a></p>

<p>&nbsp;</p>
"""

    }

]
###########################################################################
# ALL profiles list....
###########################################################################
all_profiles = [

{

    "full_name" : "William Lee",
    "phone" : "+1-699-079-9887",
    "email" : "loriwallace@gmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$bThBcFdSdExuSHB6$WO4IhpoBlkg18ZA931ApFw",
    "repeat_password" : "36337187"
},

{
    "full_name" : "Tami French",
    "phone" : "675-235-0545",
    "email" : "portiz@hotmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$eFFXN0FsQ1QwbEJs$Z1ZuJ0nsG3qQQKtR/hXsKw",
    "repeat_password" : "77432551"
},
{   "full_name" : "Christopher Johnson",
    "phone" : "(636)987-0506x12090",
    "email" : "ifranco@hotmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$WHpoZ05sMUlxOVdx$OYkWst6MMSTr6MBSSYSamQ",
    "repeat_password" : "67965991"
},

{   "full_name" : "John Carlson",
    "phone" : "+1-764-769-8269x823",
    "email" : "cassidy61@yahoo.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$bGRxZEN5TjRPOHp4$teV+75L5X7arI55DArzg/Q",
    "repeat_password" : "51965518"
},

{
    "full_name" : "Ethan Porter",
    "phone" : "555.198.2206x9959",
    "email" : "shannon78@hawkins-peterson.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$dlg1Q0Y3d0RnZ05u$AyRayXgm+3bmBFM7OV4l4g",
    "repeat_password" : "79395328"
},

    {
        "full_name" : "Brittney Lee",
    "phone" : "559.156.6204x97368",
    "email" : "thomas37@lee.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$MTVrT1EwMWt3cjhz$sH7UQ71Ydqgc4/5lK8Wb2g",
    "repeat_password" : "97174301"
},
    {
        "full_name" : "Brian Jordan",
    "phone" : "+1-271-895-9073x28169",
    "email" : "erika88@montgomery.info",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$OXhVYkJsYjZMNTRV$ddigGcqu1Ekfgxhcn8ofTg",
    "repeat_password" : "70775150"
},
    {  "full_name" : "Joseph Wiley",
    "phone" : "1982523651",
    "email" : "danieldyer@crawford.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$VnhQaXZJRm0wc1hY$//YBD67uksWvF5QorgBbXw",
    "repeat_password" : "33724911"
},
    {  "full_name" : "Mr. David Cruz",
    "phone" : "623.897.6997x874",
    "email" : "dylan50@hotmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$UzlNRlRxM215REVi$I7ONI1op6OTiQc5DJ2fhWA",
    "repeat_password" : "84086044"
},
    {  "full_name" : "Kelly Lewis",
    "phone" : "(542)009-2917",
    "email" : "mark30@yahoo.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$MWUwTDBYWDVOaHZH$jG9zCn0mqSq37su7++J/eA",
    "repeat_password" : "83338922"
},

    {  "full_name" : "Brandon Lopez",
    "phone" : "+1-170-304-2046x35767",
    "email" : "haley06@gmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$c21Ud0gwRjFrWmJp$g9a7JRux/vyVIPlHUMG8eQ",
    "repeat_password" : "14291715"
},
    {  "full_name" : "Katherine Townsend",
    "phone" : "001-987-570-3313x52576",
    "email" : "crystalshort@aguilar-hess.info",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$NUlxWXJKdGF2b3Vv$lbSPwhMVPWcTzhvj+fHVAQ",
    "repeat_password" : "41464618"
},

    {    "full_name" : "Vanessa Castillo",
    "phone" : "(078)280-3518x76510",
    "email" : "joshuathompson@yahoo.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$YjRYalJkYmpaMHdk$HHQYycRN+xjnoBp0SNANaQ",
    "repeat_password" : "72496336"
},
    {  "full_name" : "Dean Brown",
    "phone" : "201.913.5046x748",
    "email" : "donald21@yahoo.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$TW5zVDlxM3BtcUV6$pcB5+j8ZuCekKmGeh/ISdw",
    "repeat_password" : "82731861"
},
    {  "full_name" : "Anthony Ferguson",
    "phone" : "6825151956",
    "email" : "brownderek@gmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$S2JjMGJTUkhKaDBL$LLMp99fjai95Eg4EtRppqA",
    "repeat_password" : "70046090"
},
    {  "full_name" : "Amy Taylor MD",
    "phone" : "6570587556",
    "email" : "shannonmcintyre@hotmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$ZE1ieHQ1clJpVmcy$Svx6xyZqbf+9DbJREe46HQ",
    "repeat_password" : "20350192"
},
    {  "full_name" : "Priscilla Small",
    "phone" : "(696)758-5164x5405",
    "email" : "stephanieayers@rodriguez-williams.org",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$WTJUMWh0VHBPdGxW$TxudTZoXxU9NwyTAxkjYjQ",
    "repeat_password" : "81242177"
},
    {  "full_name" : "Anna Washington",
    "phone" : "+1-424-133-3121",
    "email" : "eric68@hotmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$NzVrSU5zOHpuZnFC$+tQNBhWLK/XbC4Hefu7bUg",
    "repeat_password" : "51536107"
},
    {  "full_name" : "Alexandria Gill",
    "phone" : "018.594.0301",
    "email" : "kbrown@serrano.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$UnFnV0dKcEYydjhU$fUwLgV+5vNK6Nt4YHECaLA",
    "repeat_password" : "76077838"
},
    {  "full_name" : "Bryan Yoder",
    "phone" : "(179)335-4398",
    "email" : "rgray@hotmail.com",
    "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$VkFPMXhzSEVwZ2dU$IhUEUz9V9ax7ZNI7u/l5DA",
    "repeat_password" : "97393412"
}
]


################################################################################
# populate function

def populate():
    for i in range(20):

        fake_name = all_profiles[i]['full_name']
        fake_phone = all_profiles[i]['phone']
        fake_email = all_profiles[i]['email']
        fake_password = all_profiles[i]['repeat_password']
        fake_repeat_password = fake_password

        hashed_password = make_password(fake_password)
        #get entry for User
        user = signup_model.objects.get_or_create(full_name=fake_name, phone=fake_phone, email=fake_email, password=hashed_password,
        repeat_password=fake_repeat_password)[0]

        user_profile(
                user_name=fake_name,
                user_email=fake_email,
                overview="",
                experience=[],
                address=Address(),
                skills = [],
                interests = [],
                education_details = [],
                certifications = [],
                notification = [],
                follow_notification = [],
                chats = []).save()

        Follow(user_name = fake_email, follower=[], following=[]).save()
        User(username=fake_name, email=fake_email, password=hashed_password).save()

        author = all_profiles[i]['email']
        author_name = all_profiles[i]['full_name']
        title = all_posts_list[i]['title']
        text = all_posts_list[i]['text']
        created_on = timezone.now()

        Posts(author=author, author_name=author_name, title=title, text=text, created_on=created_on, comments_count=0, comments=[],
            likes_count=0, likes=[]).save()




if __name__ == '__main__':
    print('populating script running!...')
    populate()
    print('populating script complete')
