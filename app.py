# ============================================================
#  Longman 3000 — English / Arabic Flashcard Game
#  Full word list (A - Z) included below.
#  Run:  python app.py
# ============================================================

import random

# ------------------------------------------------------------
# 1) DATA  —  letters A - C
# ------------------------------------------------------------
DATA = """
a (article)|أداة نكرة
abandon|يتخلى عن
ability|قدرة
able|قادر
about (prep)|عن ، حول
about (adv)|حوالي ، تقريبًا
above (adv, prep)|فوق
above (adj)|المذكور أعلاه
abroad|في الخارج
absence|غياب
absolute|مطلق
absolutely|بالتأكيد ، تمامًا
absorb|يمتص
abuse|إساءة ، سوء استخدام
academic|أكاديمي
accept|يقبل
acceptable|مقبول
access|وصول ، منفذ
accident|حادث
accommodation|إقامة ، سكن
accompany|يرافق
according to|وفقًا لـ
account (n)|حساب
account (v)|يفسر ، يعلل
accurate|دقيق
accuse|يتهم
achieve|يحقق
achievement|إنجاز
acid|حمض
acknowledge|يعترف
acquire|يكتسب
across|عبر
act (n)|فعل ، قانون
act (v)|يتصرف ، يمثل
action|عمل ، إجراء
active|نشيط
activist|ناشط
activity|نشاط
actor|ممثل
actual|فعلي
actually|في الواقع
ad|إعلان
adapt|يتكيف
add|يضيف
addition|إضافة
additional|إضافي
address (n)|عنوان
address (v)|يخاطب ، يعالج
adequate|كافٍ
adjust|يعدل
administration|إدارة
administrative|إداري
admire|يعجب بـ
admission|قبول ، اعتراف
admit|يعترف ، يقبل
adopt|يتبنى
adult (n)|بالغ
adult (adj)|خاص بالبالغين
advance (n)|تقدم
advance (v)|يتقدم
advanced|متقدم
advantage|ميزة
advert|إعلان
advertise|يعلن
advertisement|إعلان
advertising|الإعلانات
advice|نصيحة
advise|ينصح
adviser|مستشار
affair|شأن ، أمر
affect|يؤثر على
afford|يستطيع تحمل التكلفة
afraid|خائف
after|بعد
afternoon|بعد الظهر
afterwards|بعد ذلك
again|مرة أخرى
against|ضد
age|عمر
aged|مسن
agency|وكالة
agent|وكيل ، عميل
aggressive|عدواني
ago|منذ
agree|يوافق
agreement|اتفاق
agriculture|زراعة
ahead|إلى الأمام
aid|مساعدة
aim (n)|هدف
aim (v)|يهدف
air|هواء
aircraft|طائرة
airline|شركة طيران
airport|مطار
alarm|منبه ، إنذار
album|ألبوم
alcohol|كحول
alive|حي
all|كل
allow|يسمح
allowance|بدل ، مخصص
all right|حسنًا
almost|تقريبًا
alone|وحيد ، بمفرده
along|على طول
alongside|بجانب
already|بالفعل
also|أيضًا
alter|يغير
alternative (adj)|بديل
alternative (n)|بديل
although|على الرغم من
altogether|إجمالاً ، تمامًا
always|دائمًا
amazing|مذهل
ambition|طموح
ambulance|سيارة إسعاف
among|بين
amount|كمية
an (article)|أداة نكرة
analyse|يحلل
analysis|تحليل
analyst|محلل
ancient|قديم
and|و
anger|غضب
angle|زاوية
angry|غاضب
animal|حيوان
announce|يعلن
announcement|إعلان
annoy|يضايق
annual|سنوي
another|آخر
answer (n)|جواب
answer (v)|يجيب
anticipate|يتوقع
anxiety|قلق
anxious|قلق
any|أي
any (adv)|بأي حال
anybody|أي شخص
anyhow|بأي حال
anyone|أي شخص
anything|أي شيء
anyway|على أي حال
anywhere|في أي مكان
apart|منفصل ، باستثناء
apartment|شقة
apologize|يعتذر
apology|اعتذار
apparent|واضح ، ظاهر
apparently|كما يبدو
appeal (n)|نداء ، استئناف
appeal (v)|يناشد ، يستأنف
appear|يظهر
appearance|مظهر
apple|تفاحة
application|طلب ، تطبيق
apply|يتقدم ، يطبق
appoint|يعين
appointment|موعد
appreciate|يقدر
approach (n)|نهج ، اقتراب
approach (v)|يقترب
appropriate|مناسب
approval|موافقة
approve|يوافق على
approximate|تقريبي
architect|مهندس معماري
architecture|هندسة معمارية
area|منطقة
argue|يجادل
argument|جدال ، حجة
arise|ينشأ
arm|ذراع
armed|مسلح
army|جيش
around|حول
arrange|يرتب
arrangement|ترتيب
arrest|يعتقل
arrival|وصول
arrive|يصل
art|فن
article|مقال
artificial|اصطناعي
artist|فنان
as (conj)|كما ، لأن
as (prep)|كـ
ashamed|خجل
aside|جانبًا
ask|يسأل
asleep|نائم
aspect|جانب
assess|يقيم
assessment|تقييم
assignment|مهمة
assist|يساعد
assistance|مساعدة
assistant|مساعد
associate|يربط
association|جمعية ، ارتباط
assume|يفترض
assumption|افتراض
assure|يؤكد
at|في ، عند
atmosphere|جو
attach|يرفق ، يربط
attack (n)|هجوم
attack (v)|يهجم
attempt (n)|محاولة
attempt (v)|يحاول
attend|يحضر
attention|انتباه
attitude|موقف ، سلوك
attorney|محامٍ
attract|يجذب
attraction|جاذبية
attractive|جذاب
audience|جمهور
aunt|عمة ، خالة
author|مؤلف
authority|سلطة
automatic|تلقائي
automatically|تلقائيًا
autumn|خريف
available|متاح
average (adj)|متوسط
average (n)|متوسط
avoid|يتجنب
awake|مستيقظ
award (n)|جائزة
award (v)|يمنح
aware|مدرك
awareness|وعي
away|بعيدًا
awful|فظيع
awkward|محرج
baby|طفل
back (adv)|إلى الوراء ، عائدًا
back (n)|ظهر
back (v)|يدعم
back (adj)|خلفي
background|خلفية
backwards|إلى الخلف
bacon|لحم مقدد
bad|سيئ
badly|بشكل سيئ
bag|حقيبة
bake|يخبز
balance (n)|توازن
balance (v)|يوازن
ball|كرة
ban|حظر
band|فرقة
bang (v)|يضرب
bang (n)|ضربة ، فرقعة
bank|بنك ، ضفة
bar|حانة ، قضيب
barrier|حاجز
base (v)|يؤسس
base (n)|قاعدة
baseball|كرة قاعدة
basic|أساسي
basically|أساسًا
basis|أساس
basket|سلة
bat|مضرب ، خفاش
bath|حوض حمام
bathroom|حمام
battery|بطارية
battle|معركة
be|يكون
beach|شاطئ
bean|فاصولياء
bear|يتحمل ، دب
beard|لحية
beat (v)|يضرب ، يهزم
beat (n)|ضربة ، إيقاع
beautiful|جميل
beauty|جمال
because|لأن
become|يصبح
bed|سرير
bedroom|غرفة نوم
beef|لحم بقري
beer|بيرة
before (adv)|قبل
before (conj)|قبل أن
before (prep)|قبل
beforehand|مسبقًا
begin|يبدأ
beginning|بداية
behalf|نيابة عن
behave|يتصرف
behaviour|سلوك
behind|خلف
being|كائن
belief|اعتقاد
believe|يعتقد
bell|جرس
belong|ينتمي
below|تحت
belt|حزام
bench|مقعد
bend|ينحني
beneath|تحت
benefit (n)|فائدة
benefit (v)|يستفيد
beside|بجانب
best (adj)|الأفضل
best (adv)|بشكل أفضل
bet (v)|يراهن
bet (n)|رهان
better (adj)|أفضل
better (adv)|بشكل أفضل
between|بين
beyond|وراء
bicycle|دراجة
bid|عرض ، مزايدة
big|كبير
bike|دراجة
bill|فاتورة
bin|سلة مهملات
bird|طائر
birth|ولادة
birthday|عيد ميلاد
biscuit|بسكويت
bit (n)|قطعة ، جزء
bit (adv)|قليلاً
bite (v)|يعض
bite (n)|عضة
bitter|مر
black|أسود
blade|نصل
blame|يلوم
blank|فارغ
bless|يبارك
blind|أعمى
block (n)|كتلة ، مربع سكني
block (v)|يسد
bloke|رجل
blonde|أشقر
blood|دم
blow (v)|ينفخ
blow (n)|ضربة
blue|أزرق
board|لوح ، مجلس
boat|قارب
body|جسم
boil|يغلي
boiler|غلاية
boiling|مغلي ، حار جدًا
bomb|قنبلة
bone|عظم
bonus|مكافأة
book (n)|كتاب
book (v)|يحجز
boom|ازدهار
boot|حذاء طويل ، صندوق سيارة
border|حدود
bored|ملول
boring|ممل
born|مولود
borrow|يستعير
boss|رئيس
both|كلاهما
bother|يزعج
bottle|زجاجة
bottom (adj)|سفلي
bottom (n)|أسفل
bounce|يرتد
bound|مرتبط ، ملزم
bowl|وعاء
box|صندوق
boy|ولد
boyfriend|حبيب
brain|دماغ
branch|فرع
brave|شجاع
bread|خبز
break (n)|استراحة
break (v)|يكسر
breakfast|فطور
breast|صدر
breath|نفس
breathe|يتنفس
brick|طوب
bridge|جسر
brief|موجز
briefly|بإيجاز
bright|مشرق ، ذكي
brilliant|رائع
bring|يجلب
broad|واسع
brother|أخ
brown|بني
brush (n)|فرشاة
brush (v)|ينظف بالفرشاة
buck|دولار
bucket|دلو
buddy|صديق
budget|ميزانية
bug|حشرة ، خطأ برمجي
build|يبني
builder|بنّاء
building|مبنى
bump|يصطدم
bunch|مجموعة
burn (v)|يحرق
burn (n)|حرق
burst|ينفجر
bury|يدفن
bus|حافلة
business|عمل ، تجارة
busy|مشغول
but|لكن
but (prep)|ما عدا
but (adv)|لكن
butcher|جزار
butter|زبدة
button|زر
buy|يشتري
buyer|مشتري
by (prep)|بواسطة ، بجانب
by (adv)|قرب ، مرورًا
bye|وداعًا
cabinet|خزانة ، مجلس وزراء
cable|كابل
cake|كعكة
calculate|يحسب
calculation|حساب
calculator|آلة حاسبة
calendar|تقويم
call (n)|مكالمة
call (v)|ينادي ، يتصل
calm|هادئ
camera|كاميرا
camp|مخيم
campaign|حملة
can (modal)|يستطيع
can (n)|علبة
cancel|يلغي
cancer|سرطان
candidate|مرشح
candle|شمعة
candy|حلوى
cap|قبعة
capable|قادر
capacity|سعة
capital (n)|عاصمة ، رأس مال
capital (adj)|رئيسي
captain|قائد
capture|يأسر ، يلتقط
car|سيارة
card|بطاقة
care (n)|عناية
care (v)|يهتم
career|مهنة
careful|حذر
carefully|بحذر
carpet|سجادة
"""

# ------------------------------------------------------------
# 2) DATA_CONTINUED  —  letters D - Z
# ------------------------------------------------------------
DATA_CONTINUED = """
dad|أب
daily|يومي
damage|ضرر
dance|يرقص ، رقص
danger|خطر
dangerous|خطير
dare|يجرؤ
dark|مظلم
data|بيانات
date|تاريخ ، موعد
daughter|ابنة
day|يوم
dead|ميت
deal|يتعامل ، صفقة
dear|عزيز
death|موت
debate|مناظرة
debt|دين
decade|عقد ( عشر سنوات )
decide|يقرر
decision|قرار
declare|يعلن
decline|ينخفض ، يرفض
deep|عميق
deeply|بعمق
defendant|متهم
defense|دفاع
deficit|عجز
define|يعرف
definitely|بالتأكيد
definition|تعريف
degree|درجة
delay|تأخير
deliberately|عمدًا
deliver|يسلم
delivery|توصيل
demand|يطالب ، طلب
democracy|ديمقراطية
democratic|ديمقراطي
demonstrate|يبرهن ، يتظاهر
deny|ينكر
department|قسم
depend|يعتمد
dependent|معتمد
deposit|إيداع
depression|اكتئاب ، كساد
derive|يستمد
describe|يصف
description|وصف
desert|صحراء
deserve|يستحق
design|تصميم
designer|مصمم
desire|رغبة
desk|مكتب
desperate|يائس
despite|على الرغم من
destroy|يدمر
destruction|تدمير
detail|تفصيل
detailed|مفصل
detect|يكشف
determine|يحدد
develop|يطور
development|تطوير
device|جهاز
devote|يكرس
dialogue|حوار
diamond|ألماس
diary|مذكرات
die|يموت
diet|نظام غذائي
differ|يختلف
difference|فرق
different|مختلف
difficult|صعب
difficulty|صعوبة
dig|يحفر
dinner|عشاء
direct|مباشر ، يوجه
direction|اتجاه
directly|مباشرة
director|مدير
dirt|أوساخ
dirty|قذر
disability|إعاقة
disagree|يختلف
disappear|يختفي
disappointed|محبط
disaster|كارثة
discipline|انضباط
discount|خصم
discover|يكتشف
discovery|اكتشاف
discuss|يناقش
discussion|مناقشة
disease|مرض
dish|طبق
dismiss|يرفض ، يطرد
display|يعرض
distance|مسافة
distant|بعيد
distinct|متميز
distinction|تمييز
distinguish|يميز
distribute|يوزع
distribution|توزيع
district|منطقة
divide|يقسم
division|قسمة
divorce|طلاق
do|يفعل
doctor|طبيب
document|وثيقة
dog|كلب
dollar|دولار
domestic|محلي ، منزلي
dominant|مهيمن
dominate|يهيمن
door|باب
double|مزدوج
doubt|شك
down|أسفل
downstairs|في الطابق السفلي
downtown|وسط المدينة
dozen|دستة
draft|مسودة
drag|يسحب
drama|دراما
dramatic|درامي
draw|يرسم
drawing|رسم
dream|حلم
dress|فستان ، يلبس
drink|يشرب
drive|يقود
driver|سائق
drop|يسقط
drug|دواء ، مخدر
drum|طبل
drunk|ثمل
dry|جاف
due|مستحق
during|خلال
dust|غبار
duty|واجب
DVD|دي في دي
each|كل
ear|أذن
early|مبكر
earn|يكسب
earth|الأرض
ease|سهولة
east|شرق
eastern|شرقي
easy|سهل
eat|يأكل
economic|اقتصادي
economics|اقتصاد
economist|خبير اقتصادي
economy|اقتصاد
edge|حافة
edit|يحرر
edition|طبعة
editor|محرر
education|تعليم
educational|تعليمي
effect|تأثير
effective|فعال
effectively|بفعالية
efficiency|كفاءة
efficient|كفؤ
effort|جهد
egg|بيضة
eight|ثمانية
either|إما
elderly|مسن
elect|ينتخب
election|انتخاب
electric|كهربائي
electrical|كهربائي
electricity|كهرباء
electronic|إلكتروني
element|عنصر
elevator|مصعد
eliminate|يلغي
else|آخر
elsewhere|في مكان آخر
email|بريد إلكتروني
embrace|يعتنق
emerge|يظهر
emergency|طارئ
emission|انبعاث
emotion|عاطفة
emotional|عاطفي
emphasis|تشديد
emphasize|يؤكد
empire|إمبراطورية
employ|يوظف
employee|موظف
employer|صاحب عمل
employment|توظيف
empty|فارغ
enable|يمكن
encounter|يواجه
encourage|يشجع
end|نهاية
enemy|عدو
energy|طاقة
enforce|ينفذ
engage|ينخرط
engine|محرك
engineer|مهندس
engineering|هندسة
English|إنجليزي
enhance|يعزز
enjoy|يستمتع
enormous|ضخم
enough|كافٍ
ensure|يضمن
enter|يدخل
enterprise|مشروع
entertainment|ترفيه
entire|كامل
entirely|بالكامل
entrance|مدخل
entry|دخول
environment|بيئة
environmental|بيئي
episode|حلقة
equal|متساوٍ
equally|بالتساوي
equipment|معدات
equivalent|مكافئ
error|خطأ
escape|يهرب
especially|خاصة
essay|مقالة
essential|أساسي
establish|يؤسس
establishment|مؤسسة
estate|عقار
estimate|يقدر
ethical|أخلاقي
ethnic|عرقي
evaluate|يقيم
even|حتى
evening|مساء
event|حدث
eventually|في النهاية
ever|أبدًا
every|كل
everybody|الجميع
everyday|يومي
everyone|الجميع
everything|كل شيء
everywhere|في كل مكان
evidence|دليل
evil|شر
exact|دقيق
exactly|بالضبط
exam|امتحان
examination|فحص
examine|يفحص
example|مثال
exceed|يتجاوز
excellent|ممتاز
except|ما عدا
exception|استثناء
exchange|تبادل
excited|متحمس
excitement|حماس
exciting|مثير
exclude|يستبعد
exclusive|حصري
excuse|عذر
execute|ينفذ
executive|تنفيذي
exercise|تمرين
exhibit|يعرض
exhibition|معرض
exist|يوجد
existence|وجود
exit|خروج
expand|يتوسع
expansion|توسع
expect|يتوقع
expectation|توقع
expense|مصروف
expensive|غالٍ
experience|خبرة
experiment|تجربة
expert|خبير
explain|يشرح
explanation|تفسير
explode|ينفجر
exploit|يستغل
explore|يستكشف
explosion|انفجار
export|يصدّر
expose|يكشف
exposure|تعرض
express|يعبر
expression|تعبير
extend|يمدد
extension|امتداد
extensive|واسع
extent|مدى
external|خارجي
extra|إضافي
extraordinary|استثنائي
extreme|متطرف
extremely|للغاية
eye|عين
face|وجه
facility|منشأة
fact|حقيقة
factor|عامل
factory|مصنع
fail|يفشل
failure|فشل
fair|عادل
fairly|إلى حد ما
faith|إيمان
fall|يسقط
false|زائف
familiar|مألوف
family|عائلة
famous|مشهور
fan|مروحة ، مشجع
fancy|يتخيل
far|بعيد
farm|مزرعة
farmer|مزارع
fashion|أزياء
fast|سريع
fat|سمين
father|أب
fault|خطأ
favour|معروف
favourite|مفضل
fear|خوف
feature|ميزة
federal|فدرالي
fee|رسوم
feed|يطعم
feel|يشعر
feeling|شعور
fellow|زميل
female|أنثى
fence|سياج
festival|مهرجان
fetch|يجلب
fever|حمى
few|قليل
field|حقل
fight|يقاتل
figure|شكل ، رقم
file|ملف
fill|يملأ
film|فيلم
final|نهائي
finally|أخيرًا
finance|مالية
financial|مالي
find|يجد
fine|بخير ، غرامة
finger|إصبع
finish|ينهي
fire|نار
firm|شركة
first|أول
fish|سمكة
fit|مناسب
fix|يصلح
flag|علم
flat|شقة ، مسطح
flavour|نكهة
flee|يهرب
flesh|لحم
flight|رحلة
float|يطفو
flood|فيضان
floor|أرضية
flow|يتدفق
flower|زهرة
fly|يطير
focus|يركز
fold|يطوي
folk|ناس
follow|يتبع
following|التالي
food|طعام
foot|قدم
football|كرة القدم
for|لـ
force|قوة
foreign|أجنبي
forest|غابة
forever|إلى الأبد
forget|ينسى
forgive|يغفر
form|شكل
formal|رسمي
formation|تكوين
former|سابق
formula|صيغة
forth|إلى الأمام
fortune|ثروة
forward|إلى الأمام
found|أسس
foundation|أساس
frame|إطار
free|حر
freedom|حرية
freeze|يتجمد
frequent|متكرر
frequently|بشكل متكرر
fresh|طازج
friend|صديق
friendly|ودود
friendship|صداقة
from|من
front|أمام
fruit|فاكهة
frustrated|محبط
frustration|إحباط
fuel|وقود
full|ممتلئ
fully|بالكامل
fun|متعة
function|وظيفة
fund|تمويل
fundamental|أساسي
funding|تمويل
funny|مضحك
furniture|أثاث
furthermore|علاوة على ذلك
future|مستقبل
gain|يكسب
game|لعبة
gang|عصابة
gap|فجوة
garden|حديقة
gas|غاز
gate|بوابة
gather|يجمع
gay|مثلي
gear|عتاد
gender|جنس
gene|جين
general|عام
generally|عمومًا
generate|يولد
generation|جيل
gentleman|رجل نبيل
genuine|أصلي
get|يحصل
giant|عملاق
gift|هدية
girl|فتاة
girlfriend|حبيبة
give|يعطي
glad|مسرور
glass|زجاج
global|عالمي
glove|قفاز
go|يذهب
goal|هدف
god|إله
gold|ذهب
golf|غولف
good|جيد
government|حكومة
governor|حاكم
grab|يمسك
grade|درجة
gradually|تدريجيًا
grand|كبير
grandfather|جد
grandmother|جدة
grant|يمنح
grass|عشب
grateful|ممتن
great|عظيم
green|أخضر
grey|رمادي
ground|أرض
group|مجموعة
grow|ينمو
growth|نمو
guarantee|يضمن
guard|يحرس
guess|يخمن
guest|ضيف
guide|دليل
guideline|إرشاد
guilty|مذنب
gun|بندقية
guy|رجل
habit|عادة
hair|شعر
half|نصف
hall|قاعة
hand|يد
handle|يتعامل
hang|يعلق
happen|يحدث
happy|سعيد
hard|صعب
hardly|بالكاد
harm|ضرر
hat|قبعة
hate|يكره
have|يملك
he|هو
head|رأس
headache|صداع
health|صحة
healthy|صحي
hear|يسمع
heart|قلب
heat|حرارة
heavily|بشدة
heavy|ثقيل
height|ارتفاع
hell|جهنم
hello|مرحبًا
help|يساعد
helpful|مفيد
her|لها
here|هنا
hero|بطل
herself|نفسها
hey|مرحبًا
hi|مرحبًا
hide|يخفي
high|عالي
highlight|يسلط الضوء
highly|للغاية
highway|طريق سريع
hill|تل
him|له
himself|نفسه
hip|ورك
hire|يستأجر
his|له
historian|مؤرخ
historic|تاريخي
historical|تاريخي
history|تاريخ
hit|يضرب
hold|يمسك
hole|حفرة
holiday|عطلة
holy|مقدس
home|منزل
homework|واجب منزلي
honest|صادق
honey|عسل
honour|شرف
hope|أمل
horizon|أفق
horror|رعب
horse|حصان
hospital|مستشفى
host|مضيف
hot|حار
hotel|فندق
hour|ساعة
house|منزل
household|أسرة
housing|إسكان
how|كيف
however|لكن
huge|ضخم
human|بشري
humour|فكاهة
hundred|مئة
hungry|جائع
hunt|يصطاد
hurry|يستعجل
hurt|يجرح
husband|زوج
I|أنا
ice|ثلج
idea|فكرة
ideal|مثالي
identify|يحدد
identity|هوية
if|إذا
ignore|يتجاهل
ill|مريض
illegal|غير قانوني
illness|مرض
illustrate|يوضح
image|صورة
imagination|خيال
imagine|يتخيل
immediate|فوري
immediately|فورًا
immigrant|مهاجر
impact|تأثير
implement|ينفذ
implication|تأثير ضمني
imply|يعني ضمناً
import|يستورد
importance|أهمية
important|مهم
impose|يفرض
impossible|مستحيل
impress|يترك انطباعًا
impression|انطباع
impressive|مثير للإعجاب
improve|يحسن
improvement|تحسين
in|في
inch|بوصة
incident|حادث
include|يشمل
including|بما في ذلك
income|دخل
increase|يزيد
increasingly|بشكل متزايد
incredible|لا يصدق
indeed|فعلاً
independence|استقلال
independent|مستقل
index|فهرس
indicate|يشير
indication|إشارة
individual|فرد
industrial|صناعي
industry|صناعة
infection|عدوى
influence|تأثير
inform|يبلغ
information|معلومات
ingredient|مكوّن
initial|أولي
initially|في البداية
initiative|مبادرة
injury|إصابة
inner|داخلي
innocent|بريء
innovation|ابتكار
input|مدخلات
inquiry|استفسار
inside|داخل
insight|بصيرة
insist|يصر
inspire|يلهم
install|يثبت
instance|مثال
instead|بدلاً
institute|معهد
institution|مؤسسة
instruction|تعليمات
instrument|أداة
insurance|تأمين
intelligence|ذكاء
intelligent|ذكي
intend|ينوي
intense|شديد
intensity|شدة
intention|نية
interaction|تفاعل
interest|اهتمام ، فائدة
interested|مهتم
interesting|مثير للاهتمام
internal|داخلي
international|دولي
internet|إنترنت
interpret|يفسر
interpretation|تفسير
interview|مقابلة
into|إلى
introduce|يقدم
introduction|مقدمة
invade|يغزو
invest|يستثمر
investigate|يحقق
investigation|تحقيق
investment|استثمار
investor|مستثمر
invite|يدعو
involve|يشمل
involved|متورط
iron|حديد
island|جزيرة
issue|قضية
it|هو / هي
item|عنصر
its|له / لها
itself|نفسه
jacket|سترة
jail|سجن
January|يناير
jazz|جاز
jeans|جينز
jet|طائرة نفاثة
job|وظيفة
join|ينضم
joint|مشترك
joke|نكتة
journal|مجلة
journalist|صحفي
journey|رحلة
joy|فرح
judge|قاضٍ
judgment|حكم
juice|عصير
July|يوليو
jump|يقفز
June|يونيو
junior|مبتدئ
jury|هيئة محلفين
just|فقط
justice|عدالة
justify|يبرر
keep|يحفظ
key|مفتاح
kick|يركل
kid|طفل
kill|يقتل
killer|قاتل
killing|قتل
kilometre|كيلومتر
kind|نوع
king|ملك
kiss|قبلة
kitchen|مطبخ
knee|ركبة
knife|سكين
knock|يطرق
know|يعرف
knowledge|معرفة
lab|مختبر
label|ملصق
labour|عمل
lack|نقص
lady|سيدة
lake|بحيرة
land|أرض
landscape|منظر طبيعي
language|لغة
laptop|حاسوب محمول
large|كبير
largely|إلى حد كبير
last|آخر
late|متأخر
later|لاحقًا
latest|الأحدث
latter|الأخير
laugh|يضحك
launch|يطلق
law|قانون
lawyer|محامٍ
lay|يضع
layer|طبقة
lazy|كسول
lead|يقود
leader|قائد
leadership|قيادة
leaf|ورقة
league|دوري
lean|يميل
learn|يتعلم
least|الأقل
leather|جلد
leave|يترك
left|يسار
leg|ساق
legal|قانوني
legislation|تشريع
legitimate|شرعي
lemon|ليمون
lend|يقرض
length|طول
less|أقل
lesson|درس
let|يسمح
letter|رسالة
level|مستوى
liberal|ليبرالي
library|مكتبة
licence|رخصة
lie|يكذب ، يستلقي
life|حياة
lift|يرفع
light|ضوء
like|يحب ، مثل
likely|محتمل
limit|حد
limitation|قيد
limited|محدود
line|خط
link|رابط
lip|شفة
liquid|سائل
list|قائمة
listen|يستمع
literature|أدب
little|قليل
live|يعيش
lively|حيوي
living|معيشة
load|حمل
loan|قرض
local|محلي
locate|يحدد موقع
location|موقع
lock|قفل
London|لندن
lonely|وحيد
long|طويل
look|ينظر
loop|حلقة
loose|رخو
lord|سيد
lose|يخسر
loss|خسارة
lost|تائه
lot|كثير
loud|صاخب
love|حب
lovely|جميل
lover|محب
low|منخفض
lower|أخفض
luck|حظ
lucky|محظوظ
lunch|غداء
lung|رئة
machine|آلة
mad|مجنون
magazine|مجلة
magic|سحر
mail|بريد
main|رئيسي
mainly|بشكل رئيسي
maintain|يحافظ
maintenance|صيانة
major|رئيسي
majority|أغلبية
make|يصنع
male|ذكر
mall|مركز تجاري
man|رجل
manage|يدير
management|إدارة
manager|مدير
manner|طريقة
manufacturer|مصنع
many|كثير
map|خريطة
March|مارس
mark|علامة
market|سوق
marketing|تسويق
marriage|زواج
married|متزوج
marry|يتزوج
mass|كتلة
massive|ضخم
master|سيد
match|مباراة
material|مادة
matter|مسألة
may|قد
maybe|ربما
mayor|عمدة
me|أنا
meal|وجبة
mean|يعني
meaning|معنى
means|وسائل
meanwhile|في الوقت نفسه
measure|قياس
meat|لحم
mechanism|آلية
media|إعلام
medical|طبي
medicine|طب
medium|متوسط
meet|يلتقي
meeting|اجتماع
member|عضو
membership|عضوية
memory|ذاكرة
mental|عقلي
mention|يذكر
menu|قائمة طعام
mere|مجرد
merely|فقط
mess|فوضى
message|رسالة
metal|معدن
method|طريقة
middle|وسط
might|قد
mild|معتدل
mile|ميل
military|عسكري
milk|حليب
million|مليون
mind|عقل
mine|ملكي ، منجم
minister|وزير
ministry|وزارة
minor|ثانوي
minority|أقلية
minute|دقيقة
miracle|معجزة
mirror|مرآة
miss|يفتقد
missile|صاروخ
mission|مهمة
mistake|خطأ
mix|يخلط
mixture|خليط
mobile|محمول
mode|نمط
model|نموذج
moderate|معتدل
modern|حديث
modest|متواضع
mom|أم
moment|لحظة
money|مال
monitor|يراقب
month|شهر
mood|مزاج
moon|قمر
moral|أخلاقي
more|أكثر
morning|صباح
mortgage|رهن عقاري
most|أكثر
mostly|غالبًا
mother|أم
motion|حركة
motivation|تحفيز
motor|محرك
mount|يشرع في
mountain|جبل
mouse|فأر
mouth|فم
move|يتحرك
movement|حركة
movie|فيلم
much|كثير
mum|أم
murder|قتل
muscle|عضلة
museum|متحف
music|موسيقى
musical|موسيقي
must|يجب
my|لي
myself|نفسي
mystery|غموض
nail|مسمار ، ظفر
naked|عاري
name|اسم
narrative|سرد
narrow|ضيق
nation|أمة
national|وطني
native|أصلي
natural|طبيعي
naturally|بشكل طبيعي
nature|طبيعة
near|قريب
nearby|قريب
nearly|تقريبًا
neat|مرتب
necessarily|بالضرورة
necessary|ضروري
neck|رقبة
need|يحتاج
negative|سلبي
negotiate|يتفاوض
negotiation|تفاوض
neighbour|جار
neighbourhood|حي
neither|لا هذا ولا ذاك
nerve|عصب
nervous|متوتر
net|شبكة
network|شبكة
never|أبدًا
nevertheless|مع ذلك
new|جديد
newly|حديثًا
news|أخبار
newspaper|صحيفة
next|التالي
nice|لطيف
night|ليل
nine|تسعة
no|لا
nobody|لا أحد
nod|يومئ
noise|ضجيج
none|لا شيء
nonsense|هراء
nor|ولا
normal|عادي
normally|عادةً
north|شمال
northern|شمالي
nose|أنف
not|ليس
note|ملاحظة
nothing|لا شيء
notice|يلاحظ
notion|فكرة
novel|رواية
now|الآن
nowhere|لا مكان
nuclear|نووي
number|رقم
numerous|عديد
nurse|ممرض
nut|جوزة
obey|يطيع
object|شيء ، يعترض
objective|هدف
obligation|التزام
observation|ملاحظة
observe|يلاحظ
obtain|يحصل على
obvious|واضح
obviously|بوضوح
occasion|مناسبة
occasionally|أحيانًا
occupation|مهنة
occupy|يشغل
occur|يحدث
ocean|محيط
odd|غريب
of|من
off|بعيد
offence|جريمة
offend|يسيء
offensive|مسيء
offer|يعرض
office|مكتب
officer|ضابط
official|رسمي
often|غالبًا
oil|نفط
okay|حسنًا
old|قديم
on|على
once|مرة واحدة
one|واحد
ongoing|مستمر
onion|بصل
online|عبر الإنترنت
only|فقط
onto|إلى
open|مفتوح
opening|افتتاح
operate|يشغل
operation|عملية
operator|مشغل
opinion|رأي
opponent|خصم
opportunity|فرصة
oppose|يعارض
opposition|معارضة
option|خيار
or|أو
orange|برتقال
order|طلب ، أمر
ordinary|عادي
organ|عضو
organization|منظمة
organize|ينظم
origin|أصل
original|أصلي
originally|أصلاً
other|آخر
otherwise|وإلا
ought|ينبغي
our|لنا
ourselves|أنفسنا
out|خارج
outcome|نتيجة
outdoor|خارجي
outer|خارجي
outline|مخطط
output|إنتاج
outside|خارج
oven|فرن
over|فوق
overall|إجمالي
overcome|يتغلب على
overseas|خارج البلاد
oversee|يشرف
overturn|يقلب
owe|يدين
own|يمتلك
owner|مالك
ownership|ملكية
oxygen|أكسجين
pace|وتيرة
pack|يحزم
package|حزمة
page|صفحة
pain|ألم
painful|مؤلم
paint|يصبغ
painter|رسام
painting|لوحة
pair|زوج
pale|شاحب
palm|كف
panel|لوحة
panic|ذعر
paper|ورق
parent|والد
park|حديقة
parliament|برلمان
part|جزء
participant|مشارك
participate|يشارك
particular|معين
particularly|خصوصًا
partly|جزئيًا
partner|شريك
partnership|شراكة
party|حزب ، حفلة
pass|يمر
passage|ممر
passenger|راكب
passion|شغف
past|ماضٍ
path|مسار
patient|مريض
pattern|نمط
pause|توقف
pay|يدفع
payment|دفع
peace|سلام
peaceful|سلمي
peak|قمة
peer|نظير
penalty|عقوبة
pencil|قلم رصاص
pension|معاش
people|ناس
pepper|فلفل
per|لكل
percent|بالمئة
percentage|نسبة مئوية
perception|إدراك
perfect|مثالي
perform|يؤدي
performance|أداء
perhaps|ربما
period|فترة
permanent|دائم
permission|إذن
permit|يسمح
person|شخص
personal|شخصي
personality|شخصية
personally|شخصيًا
personnel|أفراد
perspective|منظور
persuade|يقنع
pet|حيوان أليف
phase|مرحلة
phenomenon|ظاهرة
philosophy|فلسفة
phone|هاتف
photo|صورة
photograph|صورة
photographer|مصور
phrase|عبارة
physical|جسدي
physician|طبيب
piano|بيانو
pick|يختار
picture|صورة
pie|فطيرة
piece|قطعة
pile|كومة
pilot|طيار
pin|دبوس
pink|وردي
pipe|أنبوب
pitch|ملعب
place|مكان
plain|بسيط
plan|خطة
plane|طائرة
planet|كوكب
planning|تخطيط
plant|نبات
plastic|بلاستيك
plate|طبق
platform|منصة
play|يلعب
player|لاعب
pleasant|لطيف
please|من فضلك
pleased|مسرور
pleasure|متعة
plenty|وفرة
plot|حبكة
plus|زائد
pocket|جيب
poem|قصيدة
poet|شاعر
poetry|شعر
point|نقطة
police|شرطة
policeman|شرطي
policy|سياسة
political|سياسي
politician|سياسي
politics|سياسة
poll|استطلاع
pollution|تلوث
pool|بركة
poor|فقير
pop|بوب
popular|شائع
population|سكان
port|ميناء
portion|جزء
portrait|صورة شخصية
pose|يطرح
position|موقف
positive|إيجابي
possess|يمتلك
possession|ملكية
possibility|إمكانية
possible|ممكن
possibly|ربما
post|بريد
pot|قدر
potato|بطاطس
potential|محتمل
pound|جنيه
pour|يصب
poverty|فقر
powder|مسحوق
power|قوة
powerful|قوي
practical|عملي
practice|ممارسة
praise|ثناء
pray|يصلي
prayer|صلاة
precise|دقيق
precisely|بدقة
predict|يتوقع
prediction|تنبؤ
prefer|يفضل
preference|تفضيل
pregnancy|حمل
pregnant|حامل
preparation|تحضير
prepare|يحضر
presence|حضور
present|حاضر
presentation|عرض
preserve|يحفظ
president|رئيس
press|يضغط
pressure|ضغط
pretend|يتظاهر
pretty|جميل
prevent|يمنع
previous|سابق
previously|سابقًا
price|سعر
pride|فخر
priest|كاهن
primary|أساسي
prime|رئيسي
prince|أمير
princess|أميرة
principal|مدير
principle|مبدأ
print|يطبع
printer|طابعة
prior|سابق
priority|أولوية
prison|سجن
prisoner|سجين
privacy|خصوصية
private|خاص
privilege|امتياز
prize|جائزة
probably|ربما
problem|مشكلة
procedure|إجراء
proceed|يتابع
process|عملية
produce|ينتج
producer|منتج
product|منتج
production|إنتاج
profession|مهنة
professional|مهني
professor|أستاذ
profile|ملف شخصي
profit|ربح
program|برنامج
programme|برنامج
progress|تقدم
project|مشروع
promise|وعد
promote|يروج
promotion|ترقية
prompt|يحفز
proof|دليل
proper|مناسب
properly|بشكل صحيح
property|ملكية
proportion|نسبة
proposal|اقتراح
propose|يقترح
prospect|احتمال
protect|يحمي
protection|حماية
protein|بروتين
protest|احتجاج
proud|فخور
prove|يثبت
provide|يوفر
provider|مقدم
province|مقاطعة
provision|توفير
psychology|علم النفس
pub|حانة
public|عام
publication|منشور
publish|ينشر
pull|يسحب
punishment|عقاب
purchase|شراء
pure|نقي
purple|بنفسجي
purpose|غرض
pursue|يسعى
push|يدفع
put|يضع
qualify|يتأهل
quality|جودة
quantity|كمية
quarter|ربع
queen|ملكة
query|استفسار
question|سؤال
queue|طابور
quick|سريع
quickly|بسرعة
quiet|هادئ
quietly|بهدوء
quit|يستقيل
quite|تمامًا
quote|يقتبس
race|سباق ، عرق
racial|عرقي
radio|راديو
rail|سكة حديد
railway|سكة حديد
rain|مطر
raise|يرفع
range|نطاق
rank|رتبة
rapid|سريع
rapidly|بسرعة
rare|نادر
rarely|نادرًا
rate|معدل
rather|بدلاً
rating|تصنيف
ratio|نسبة
raw|خام
reach|يصل
react|يتفاعل
reaction|رد فعل
read|يقرأ
reader|قارئ
reading|قراءة
ready|جاهز
real|حقيقي
reality|واقع
realize|يدرك
really|حقًا
reason|سبب
reasonable|معقول
recall|يتذكر
receive|يستقبل
recent|حديث
recently|مؤخرًا
recipe|وصفة
recognition|اعتراف
recognize|يتعرف
recommend|يوصي
record|يسجل
recording|تسجيل
recover|يتعافى
recovery|تعافٍ
red|أحمر
reduce|يقلل
reduction|تخفيض
refer|يشير
reference|مرجع
reflect|يعكس
reflection|انعكاس
reform|إصلاح
refuse|يرفض
regard|يعتبر
regarding|بخصوص
region|منطقة
regional|إقليمي
register|يسجل
regular|منتظم
regularly|بانتظام
regulation|تنظيم
reject|يرفض
relate|يرتبط
relation|علاقة
relationship|علاقة
relative|نسبي
relatively|نسبيًا
relax|يسترخي
release|يطلق
relevant|ذو صلة
relief|ارتياح
religion|دين
religious|ديني
rely|يعتمد
remain|يبقى
remaining|متبقٍ
remark|ملاحظة
remarkable|رائع
remember|يتذكر
remind|يذكر
remote|بعيد
remove|يزيل
repeat|يكرر
replace|يستبدل
reply|يرد
report|يبلغ
reporter|مراسل
represent|يمثل
representation|تمثيل
representative|ممثل
reproduce|يتكاثر
reputation|سمعة
request|طلب
require|يتطلب
requirement|متطلب
rescue|إنقاذ
research|بحث
researcher|باحث
reserve|يحجز
resident|مقيم
resign|يستقيل
resist|يقاوم
resistance|مقاومة
resolution|قرار
resolve|يحل
resort|منتجع
resource|مورد
respect|احترام
respond|يستجيب
response|استجابة
responsibility|مسؤولية
responsible|مسؤول
rest|راحة
restaurant|مطعم
restore|يستعيد
restrict|يقيد
restriction|قيد
result|نتيجة
retain|يحتفظ
retire|يتقاعد
retirement|تقاعد
return|يعود
reveal|يكشف
revenue|إيراد
review|مراجعة
revolution|ثورة
reward|مكافأة
rhythm|إيقاع
rice|أرز
rich|غني
rid|يتخلص
ride|يركب
right|صحيح ، حق
ring|خاتم
rise|يرتفع
risk|خطر
river|نهر
road|طريق
rock|صخرة
role|دور
roll|يتدحرج
romantic|رومانسي
roof|سقف
room|غرفة
root|جذر
rope|حبل
rough|خشن
round|جولة ، مستدير
route|مسار
routine|روتين
row|صف
royal|ملكي
rub|يفرك
rubber|مطاط
rule|قاعدة
run|يجري
running|جري
rural|ريفي
rush|يندفع
sad|حزين
safe|آمن
safety|سلامة
sail|يشرع
salad|سلطة
salary|راتب
sale|بيع
salt|ملح
same|نفس
sample|عينة
sand|رمل
satellite|قمر صناعي
satisfaction|رضا
satisfied|راضٍ
satisfy|يرضي
sauce|صلصة
save|يحفظ
saving|توفير
say|يقول
scale|مقياس
scandal|فضيحة
scared|خائف
scenario|سيناريو
scene|مشهد
schedule|جدول
scheme|خطة
scholar|عالم
school|مدرسة
science|علم
scientific|علمي
scientist|عالم
score|نتيجة
screen|شاشة
script|نص
sea|بحر
search|بحث
season|موسم
seat|مقعد
second|ثانٍ
secret|سر
secretary|سكرتير
section|قسم
sector|قطاع
secure|آمن
security|أمن
see|يرى
seed|بذرة
seek|يبحث
seem|يبدو
segment|جزء
seize|يستولي
select|يختار
selection|اختيار
self|نفس
sell|يبيع
senate|مجلس شيوخ
senator|سيناتور
send|يرسل
senior|أقدم
sense|إحساس
sensitive|حساس
sentence|جملة
separate|منفصل
September|سبتمبر
sequence|تسلسل
series|سلسلة
serious|خطير
seriously|بجدية
servant|خادم
serve|يخدم
service|خدمة
session|جلسة
set|يضع
settle|يستقر
settlement|تسوية
seven|سبعة
several|عدة
severe|شديد
sex|جنس
sexual|جنسي
shake|يهز
shall|سوف
shape|شكل
share|يشارك
sharp|حاد
she|هي
shed|يسكب ، سقيفة
sheep|خروف
sheet|ورقة
shelf|رف
shell|قشرة
shelter|مأوى
shift|تحول
shine|يلمع
ship|سفينة
shirt|قميص
shock|صدمة
shoe|حذاء
shoot|يطلق النار
shop|متجر
shopping|تسوق
short|قصير
shot|طلقة
should|ينبغي
shoulder|كتف
shout|يصرخ
show|يعرض
shower|دش
shut|يغلق
shy|خجول
sick|مريض
side|جانب
sight|بصر
sign|علامة
signal|إشارة
significance|أهمية
significant|مهم
significantly|بشكل كبير
silence|صمت
silent|صامت
silver|فضي
similar|مشابه
similarly|بالمثل
simple|بسيط
simply|ببساطة
sin|خطيئة
since|منذ
sing|يغني
singer|مغني
single|أعزب
sink|يغرق
sir|سيدي
sister|أخت
sit|يجلس
site|موقع
situation|موقف
six|ستة
size|حجم
skill|مهارة
skin|جلد
sky|سماء
sleep|ينام
slice|شريحة
slide|ينزلق
slight|طفيف
slightly|قليلاً
slip|يزلق
slow|بطيء
slowly|ببطء
small|صغير
smart|ذكي
smell|رائحة
smile|ابتسامة
smoke|دخان
snow|ثلج
so|لذلك
soap|صابون
social|اجتماعي
society|مجتمع
soft|ناعم
software|برمجيات
soil|تربة
soldier|جندي
solution|حل
solve|يحل
some|بعض
somebody|شخص ما
somehow|بطريقة ما
someone|شخص ما
something|شيء ما
sometimes|أحيانًا
somewhat|إلى حد ما
somewhere|في مكان ما
son|ابن
song|أغنية
soon|قريبًا
sophisticated|متطور
sorry|آسف
sort|نوع
soul|روح
sound|صوت
soup|حساء
source|مصدر
south|جنوب
southern|جنوبي
space|فضاء
spare|احتياطي
speak|يتحدث
speaker|متحدث
special|خاص
specialist|متخصص
species|أنواع
specific|محدد
specifically|تحديدًا
speech|خطاب
speed|سرعة
spell|يتهجى
spend|ينفق
spin|يدور
spirit|روح
spiritual|روحي
spit|يبصق
split|ينقسم
spokesman|متحدث
sport|رياضة
spot|بقعة
spread|ينتشر
spring|ربيع
square|مربع
stable|مستقر
staff|طاقم
stage|مرحلة
stair|درج
stake|حصة
stand|يقف
standard|معيار
star|نجم
stare|يحدق
start|يبدأ
state|دولة
statement|بيان
station|محطة
statistics|إحصاءات
status|حالة
stay|يبقى
steady|ثابت
steal|يسرق
steel|فولاذ
step|خطوة
stick|عصا
still|لا يزال
stir|يحرك
stock|سهم
stomach|معدة
stone|حجر
stop|يتوقف
storage|تخزين
store|متجر
storm|عاصفة
story|قصة
straight|مستقيم
strain|ضغط
strange|غريب
stranger|غريب
strategy|استراتيجية
stream|تيار
street|شارع
strength|قوة
strengthen|يعزز
stress|ضغط
stretch|يمدد
strike|يضرب
string|خيط
strip|شريط
stroke|سكتة
strong|قوي
strongly|بقوة
structure|هيكل
struggle|كفاح
student|طالب
studio|استوديو
study|يدرس
stuff|أشياء
stupid|غبي
style|أسلوب
subject|موضوع
submit|يقدم
subsequent|لاحق
substance|مادة
substantial|كبير
succeed|ينجح
success|نجاح
successful|ناجح
successfully|بنجاح
such|مثل
sudden|مفاجئ
suddenly|فجأة
suffer|يعاني
sufficient|كافٍ
sugar|سكر
suggest|يقترح
suggestion|اقتراح
suit|بدلة
suitable|مناسب
sum|مجموع
summary|ملخص
summer|صيف
sun|شمس
Sunday|الأحد
supermarket|سوبر ماركت
supply|يوفر
support|يدعم
supporter|مؤيد
suppose|يفترض
supposed|مفترض
sure|متأكد
surely|بالتأكيد
surface|سطح
surgery|جراحة
surprise|مفاجأة
surprised|متفاجئ
surprising|مفاجئ
surround|يحيط
surrounding|محيط
survey|استطلاع
survival|بقاء
survive|ينجو
suspect|يشتبه
suspicion|شك
sustain|يحافظ
sweet|حلو
swim|يسبح
swing|يتأرجح
switch|مفتاح
symbol|رمز
sympathy|تعاطف
symptom|عرض
system|نظام
table|طاولة
tackle|يعالج
tail|ذيل
take|يأخذ
tale|حكاية
talent|موهبة
talk|يتحدث
tall|طويل
tank|دبابة
tap|صنبور
tape|شريط
target|هدف
task|مهمة
taste|ذوق
tax|ضريبة
taxi|سيارة أجرة
tea|شاي
teach|يعلم
teacher|معلم
teaching|تعليم
team|فريق
tear|دمعة
technical|تقني
technique|تقنية
technology|تكنولوجيا
teen|مراهق
teenager|مراهق
telephone|هاتف
television|تلفزيون
tell|يخبر
temperature|حرارة
temporary|مؤقت
ten|عشرة
tend|يميل
tendency|ميل
tennis|تنس
tension|توتر
tent|خيمة
term|مصطلح
terrible|فظيع
territory|إقليم
terror|رعب
terrorism|إرهاب
terrorist|إرهابي
test|اختبار
text|نص
than|من
thank|يشكر
thanks|شكرًا
that|ذاك
the|ال
theatre|مسرح
their|لهم
them|هم
theme|موضوع
themselves|أنفسهم
then|ثم
theory|نظرية
therapy|علاج
there|هناك
therefore|لذلك
these|هؤلاء
they|هم
thick|سميك
thin|رقيق
thing|شيء
think|يفكر
thinking|تفكير
third|ثالث
thirty|ثلاثون
this|هذا
those|أولئك
though|رغم
thought|فكرة
thousand|ألف
threat|تهديد
threaten|يهدد
three|ثلاثة
throat|حلق
through|عبر
throughout|في جميع أنحاء
throw|يرمي
thus|هكذا
ticket|تذكرة
tie|ربطة عنق
tight|ضيق
till|حتى
time|وقت
tiny|صغير جدًا
tip|نصيحة
tired|متعب
tissue|نسيج
title|عنوان
to|إلى
today|اليوم
toe|إصبع قدم
together|معًا
tomorrow|غدًا
tone|نبرة
tongue|لسان
tonight|الليلة
too|أيضًا
tool|أداة
tooth|سن
top|أعلى
topic|موضوع
total|إجمالي
totally|تمامًا
touch|يلمس
tough|صعب
tour|جولة
tourist|سائح
toward|نحو
towards|نحو
tower|برج
town|بلدة
toy|لعبة
trace|أثر
track|مسار
trade|تجارة
tradition|تقليد
traditional|تقليدي
traffic|مرور
tragedy|مأساة
trail|مسار
train|قطار
training|تدريب
transfer|ينقل
transform|يحول
transformation|تحول
transition|انتقال
translate|يترجم
translation|ترجمة
transport|نقل
transportation|نقل
trap|فخ
travel|يسافر
treat|يعامل
treatment|علاج
treaty|معاهدة
tree|شجرة
tremendous|هائل
trend|اتجاه
trial|محاكمة
tribe|قبيلة
trick|حيلة
trip|رحلة
troop|قوات
trouble|مشكلة
truck|شاحنة
true|صحيح
truly|حقًا
trust|ثقة
truth|حقيقة
try|يحاول
tube|أنبوب
Tuesday|الثلاثاء
tune|لحن
turn|يدور
TV|تلفزيون
twelve|اثنا عشر
twenty|عشرون
twice|مرتين
twin|توأم
two|اثنان
type|نوع
typical|نموذجي
typically|عادةً
ugly|قبيح
ultimate|نهائي
ultimately|في النهاية
unable|غير قادر
uncle|عم
under|تحت
undergo|يخضع
understand|يفهم
understanding|فهم
undertake|يتعهد
unemployment|بطالة
unfortunately|للأسف
uniform|زي
union|اتحاد
unique|فريد
unit|وحدة
unite|يوحد
united|موحد
unity|وحدة
universal|عالمي
universe|كون
university|جامعة
unknown|مجهول
unless|ما لم
unlike|على عكس
unlikely|غير محتمل
until|حتى
unusual|غير عادي
up|أعلى
update|تحديث
upon|على
upper|علوي
upset|منزعج
urban|حضري
urge|يحث
urgent|عاجل
us|نحن
use|يستخدم
used|مستخدم
useful|مفيد
user|مستخدم
usual|معتاد
usually|عادةً
vacation|عطلة
valley|واد
valuable|قيم
value|قيمة
van|شاحنة صغيرة
variable|متغير
variation|تنوع
variety|تنوع
various|متنوع
vary|يختلف
vast|واسع
vegetable|خضروات
vehicle|مركبة
venture|مشروع
version|نسخة
very|جدًا
via|عبر
victim|ضحية
victory|نصر
video|فيديو
view|رأي
village|قرية
violence|عنف
violent|عنيف
virtual|افتراضي
virtually|تقريبًا
virtue|فضيلة
virus|فيروس
visible|مرئي
vision|رؤية
visit|يزور
visitor|زائر
visual|بصري
vital|حيوي
voice|صوت
volume|حجم
volunteer|متطوع
vote|يصوت
voter|ناخب
wage|أجر
wait|ينتظر
wake|يستيقظ
walk|يمشي
wall|جدار
wander|يتجول
want|يريد
war|حرب
warm|دافئ
warn|يحذر
warning|تحذير
wash|يغسل
waste|نفايات
watch|يشاهد
water|ماء
wave|موجة
way|طريق
we|نحن
weak|ضعيف
weakness|ضعف
wealth|ثروة
wealthy|ثري
weapon|سلاح
wear|يلبس
weather|طقس
web|شبكة
website|موقع ويب
wedding|زفاف
Wednesday|الأربعاء
week|أسبوع
weekend|عطلة نهاية الأسبوع
weekly|أسبوعي
weigh|يزن
weight|وزن
welcome|مرحبًا
welfare|رفاهية
well|جيدًا
west|غرب
western|غربي
wet|مبلل
what|ماذا
whatever|مهما
wheel|عجلة
when|متى
whenever|كلما
where|أين
whereas|بينما
wherever|حيثما
whether|سواء
which|أي
while|بينما
whisper|يهمس
white|أبيض
who|من
whole|كامل
whom|من
whose|لمن
why|لماذا
wide|واسع
widely|على نطاق واسع
wife|زوجة
wild|بري
will|سوف
willing|مستعد
win|يفوز
wind|ريح
window|نافذة
wine|نبيذ
wing|جناح
winner|فائز
winter|شتاء
wipe|يمسح
wire|سلك
wise|حكيم
wish|يتمنى
with|مع
withdraw|يسحب
within|خلال
without|بدون
witness|شاهد
woman|امرأة
wonder|يتساءل
wonderful|رائع
wood|خشب
wooden|خشبي
wool|صوف
word|كلمة
work|يعمل
worker|عامل
working|عامل
world|عالم
worried|قلق
worry|يقلق
worse|أسوأ
worst|الأسوأ
worth|يستحق
would|سوف
wound|جرح
wrap|يلف
write|يكتب
writer|كاتب
writing|كتابة
wrong|خطأ
yard|ساحة
yeah|نعم
year|سنة
yellow|أصفر
yes|نعم
yesterday|أمس
yet|بعد
you|أنت
young|شاب
your|لك
yours|لك
yourself|نفسك
youth|شباب
zero|صفر
zone|منطقة
"""

# ------------------------------------------------------------
# 3) Build the word list (A-Z combined)
# ------------------------------------------------------------
WORDS = [tuple(part.strip() for part in line.split("|"))
         for line in (DATA + DATA_CONTINUED).strip().splitlines()
         if line.strip()]

QUESTIONS_PER_GAME = 10          # every game = 10 cards

# ------------------------------------------------------------
# 4) Game state
# ------------------------------------------------------------
deck = []          # the 10 cards of the current game
q_index = 0        # which card we are on
right = 0          # correct answers
wrong_list = []    # (english, correct_arabic, what_user_chose)
current_options = []
current_answer = ""
current_word = ""
answered = False

# ------------------------------------------------------------
# 5) Window
# ------------------------------------------------------------
root = tk.Tk()
root.title("Longman 3000 — بطاقات إنجليزية / عربية")
root.geometry("600x520")
root.resizable(False, False)

tk.Label(root, text="Longman Communication 3000",
         font=("Arial", 16, "bold")).pack(pady=(10, 0))

info_lbl = tk.Label(root, text="", font=("Arial", 11))
info_lbl.pack(pady=4)

word_lbl = tk.Label(root, text="", font=("Arial", 28, "bold"), fg="#1a4f8a")
word_lbl.pack(pady=18)

feedback_lbl = tk.Label(root, text="", font=("Arial", 13, "bold"))
feedback_lbl.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

option_buttons = []
for i in range(4):
    b = tk.Button(btn_frame, text="", width=28, height=2,
                  font=("Arial", 13), cursor="hand2",
                  command=lambda i=i: check_answer(i))
    b.pack(pady=5)
    option_buttons.append(b)

next_btn = tk.Button(root, text="التالي ▶", width=18, height=2,
                     font=("Arial", 12, "bold"), command=lambda: next_question())
next_btn.pack(pady=10)

# ------------------------------------------------------------
# 6) Game logic
# ------------------------------------------------------------
def make_options(answer):
    """3 random wrong Arabic meanings + the correct one."""
    pool = list({ar for _, ar in WORDS if ar != answer})   # set = no duplicates
    options = random.sample(pool, 3) + [answer]
    random.shuffle(options)
    return options


def show_question():
    global current_options, current_answer, answered, current_word

    current_word, current_answer = deck[q_index]
    current_options = make_options(current_answer)
    answered = False

    info_lbl.config(text=f"سؤال {q_index + 1} من {len(deck)}    |    "
                         f"✔ صحيح: {right}    ✘ خطأ: {len(wrong_list)}")
    word_lbl.config(text=current_word)
    feedback_lbl.config(text="")
    next_btn.config(state="disabled",
                    text="عرض النتيجة" if q_index == len(deck) - 1 else "التالي ▶")

    for i, b in enumerate(option_buttons):
        b.config(text=current_options[i], state="normal",
                 bg="SystemButtonFace", fg="black")


def check_answer(i):
    global answered, right, current_word

    if answered:
        return
    answered = True

    chosen = current_options[i]

    # mark the correct button green
    for j, b in enumerate(option_buttons):
        b.config(state="disabled")
        if current_options[j] == current_answer:
            b.config(bg="#b6e3b6")

    if chosen == current_answer:
        right += 1
        feedback_lbl.config(text="✔ إجابة صحيحة", fg="green")
    else:
        wrong_list.append((current_word, current_answer, chosen))
        option_buttons[i].config(bg="#f5b5b5")
        feedback_lbl.config(text=f"✘ خطأ — الصحيح: {current_answer}", fg="red")

    info_lbl.config(text=f"سؤال {q_index + 1} من {len(deck)}    |    "
                         f"✔ صحيح: {right}    ✘ خطأ: {len(wrong_list)}")
    next_btn.config(state="normal")


def next_question():
    global q_index
    q_index += 1
    if q_index >= len(deck):
        end_game()
    else:
        show_question()


def end_game():
    msg = (f"انتهت اللعبة!\n\n"
           f"الإجابات الصحيحة: {right} من {len(deck)}\n"
           f"الإجابات الخاطئة: {len(wrong_list)}\n")
    if right == len(deck):
        msg += "\nممتاز! كل الإجابات صحيحة 🎉"
    if wrong_list:
        msg += "\n\nالكلمات التي أخطأت فيها:\n"
        for w, a, _ in wrong_list:
            msg += f"• {w} = {a}\n"
    messagebox.showinfo("النتيجة", msg)
    start_game()


def start_game():
    global deck, q_index, right, wrong_list
    deck = random.sample(WORDS, QUESTIONS_PER_GAME)   # 10 different cards
    q_index = 0
    right = 0
    wrong_list = []
    show_question()


# ------------------------------------------------------------
# 7) Go!
# ------------------------------------------------------------
start_game()
root.mainloop()
