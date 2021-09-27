# Generated by Django 3.2.5 on 2021-09-13 12:13

import uuid

import django.utils.timezone
import taggit.managers
from django.db import migrations, models

import una_hora.users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="user's full name"
                    ),
                ),
                ("bio", models.TextField(blank=True, verbose_name="user's bio")),
                (
                    "meeting_day",
                    models.PositiveSmallIntegerField(
                        null=True, verbose_name="day of week available for meetings"
                    ),
                ),
                (
                    "meeting_time",
                    models.TimeField(
                        blank=True,
                        null=True,
                        verbose_name="time available for meetings",
                    ),
                ),
                (
                    "meeting_method",
                    models.TextField(
                        blank=True,
                        verbose_name="user's preferred meeting method with instructions",
                    ),
                ),
                (
                    "timezone",
                    models.CharField(
                        choices=[
                            ("US/Eastern", "Eastern"),
                            ("America/Phoenix", "Phoenix"),
                            ("America/Managua", "Managua"),
                            ("America/Argentina/Tucuman", "Tucuman"),
                            ("Africa/Ouagadougou", "Ouagadougou"),
                            ("America/Vancouver", "Vancouver"),
                            ("Europe/Mariehamn", "Mariehamn"),
                            ("Atlantic/Bermuda", "Bermuda"),
                            ("America/Inuvik", "Inuvik"),
                            ("Australia/Broken_Hill", "Broken_Hill"),
                            ("Asia/Hong_Kong", "Hong_Kong"),
                            ("Africa/Freetown", "Freetown"),
                            ("America/Detroit", "Detroit"),
                            ("Africa/Khartoum", "Khartoum"),
                            ("America/St_Johns", "St_Johns"),
                            ("Africa/Mbabane", "Mbabane"),
                            ("Asia/Qatar", "Qatar"),
                            ("America/Yakutat", "Yakutat"),
                            ("Africa/Dar_es_Salaam", "Dar_es_Salaam"),
                            ("America/Bogota", "Bogota"),
                            ("Atlantic/Azores", "Azores"),
                            ("Pacific/Kiritimati", "Kiritimati"),
                            ("Asia/Ashgabat", "Ashgabat"),
                            ("America/St_Kitts", "St_Kitts"),
                            ("Europe/Riga", "Riga"),
                            ("Antarctica/Troll", "Troll"),
                            ("Africa/Djibouti", "Djibouti"),
                            ("Europe/Budapest", "Budapest"),
                            ("Antarctica/McMurdo", "McMurdo"),
                            ("Europe/Moscow", "Moscow"),
                            ("Europe/Simferopol", "Simferopol"),
                            ("Europe/Sofia", "Sofia"),
                            ("America/Dawson_Creek", "Dawson_Creek"),
                            ("Europe/San_Marino", "San_Marino"),
                            ("America/Los_Angeles", "Los_Angeles"),
                            ("Europe/Luxembourg", "Luxembourg"),
                            ("America/Grenada", "Grenada"),
                            ("Australia/Lindeman", "Lindeman"),
                            ("Asia/Pontianak", "Pontianak"),
                            ("Asia/Tehran", "Tehran"),
                            ("Africa/Dakar", "Dakar"),
                            ("Antarctica/Davis", "Davis"),
                            ("America/Yellowknife", "Yellowknife"),
                            ("Africa/Tripoli", "Tripoli"),
                            ("Europe/Athens", "Athens"),
                            ("America/Araguaina", "Araguaina"),
                            ("Pacific/Chatham", "Chatham"),
                            ("Africa/Sao_Tome", "Sao_Tome"),
                            ("America/Chihuahua", "Chihuahua"),
                            ("Asia/Dhaka", "Dhaka"),
                            ("Europe/Zurich", "Zurich"),
                            ("Canada/Eastern", "Eastern"),
                            ("America/Aruba", "Aruba"),
                            ("America/Cayenne", "Cayenne"),
                            ("America/Iqaluit", "Iqaluit"),
                            ("Asia/Seoul", "Seoul"),
                            ("Africa/Porto-Novo", "Porto-Novo"),
                            ("America/Antigua", "Antigua"),
                            ("America/Miquelon", "Miquelon"),
                            ("Africa/Lome", "Lome"),
                            ("Pacific/Niue", "Niue"),
                            ("Africa/Casablanca", "Casablanca"),
                            ("America/Swift_Current", "Swift_Current"),
                            ("Australia/Melbourne", "Melbourne"),
                            ("America/Danmarkshavn", "Danmarkshavn"),
                            ("Antarctica/DumontDUrville", "DumontDUrville"),
                            ("America/Chicago", "Chicago"),
                            ("Europe/Vienna", "Vienna"),
                            ("Africa/Johannesburg", "Johannesburg"),
                            ("Asia/Almaty", "Almaty"),
                            ("US/Mountain", "Mountain"),
                            ("America/Dawson", "Dawson"),
                            ("Europe/Guernsey", "Guernsey"),
                            ("America/Rankin_Inlet", "Rankin_Inlet"),
                            ("Asia/Qostanay", "Qostanay"),
                            ("America/Guatemala", "Guatemala"),
                            ("Asia/Yerevan", "Yerevan"),
                            ("Atlantic/Reykjavik", "Reykjavik"),
                            ("America/Sao_Paulo", "Sao_Paulo"),
                            ("Asia/Amman", "Amman"),
                            ("Asia/Dili", "Dili"),
                            ("Antarctica/Rothera", "Rothera"),
                            ("America/Nassau", "Nassau"),
                            ("America/Ojinaga", "Ojinaga"),
                            ("America/Resolute", "Resolute"),
                            ("US/Arizona", "Arizona"),
                            ("America/Grand_Turk", "Grand_Turk"),
                            ("Pacific/Majuro", "Majuro"),
                            ("Indian/Reunion", "Reunion"),
                            ("America/Atikokan", "Atikokan"),
                            ("Africa/El_Aaiun", "El_Aaiun"),
                            ("Indian/Chagos", "Chagos"),
                            ("Asia/Krasnoyarsk", "Krasnoyarsk"),
                            ("Pacific/Palau", "Palau"),
                            ("Europe/Busingen", "Busingen"),
                            ("Asia/Ulaanbaatar", "Ulaanbaatar"),
                            ("Asia/Ust-Nera", "Ust-Nera"),
                            ("Africa/Lubumbashi", "Lubumbashi"),
                            ("Europe/Istanbul", "Istanbul"),
                            ("Europe/Podgorica", "Podgorica"),
                            ("Africa/Brazzaville", "Brazzaville"),
                            ("Africa/Lusaka", "Lusaka"),
                            ("America/Indiana/Marengo", "Marengo"),
                            ("Asia/Jakarta", "Jakarta"),
                            ("Asia/Beirut", "Beirut"),
                            ("America/Rio_Branco", "Rio_Branco"),
                            ("Asia/Sakhalin", "Sakhalin"),
                            ("Pacific/Rarotonga", "Rarotonga"),
                            ("Asia/Tomsk", "Tomsk"),
                            ("Pacific/Wake", "Wake"),
                            ("America/Glace_Bay", "Glace_Bay"),
                            ("America/Manaus", "Manaus"),
                            ("America/Monterrey", "Monterrey"),
                            ("Africa/Niamey", "Niamey"),
                            ("Asia/Manila", "Manila"),
                            ("Antarctica/Syowa", "Syowa"),
                            ("America/Halifax", "Halifax"),
                            ("Asia/Baku", "Baku"),
                            ("Europe/Andorra", "Andorra"),
                            ("Asia/Hebron", "Hebron"),
                            ("Asia/Kuching", "Kuching"),
                            ("America/Argentina/Ushuaia", "Ushuaia"),
                            ("US/Pacific", "Pacific"),
                            ("Europe/Gibraltar", "Gibraltar"),
                            ("Europe/Bratislava", "Bratislava"),
                            ("Indian/Maldives", "Maldives"),
                            ("Africa/Bangui", "Bangui"),
                            ("Asia/Vladivostok", "Vladivostok"),
                            ("Canada/Central", "Central"),
                            ("Asia/Makassar", "Makassar"),
                            ("America/Tortola", "Tortola"),
                            ("America/Regina", "Regina"),
                            ("Australia/Eucla", "Eucla"),
                            ("Asia/Phnom_Penh", "Phnom_Penh"),
                            ("America/Campo_Grande", "Campo_Grande"),
                            ("America/Pangnirtung", "Pangnirtung"),
                            ("America/Boa_Vista", "Boa_Vista"),
                            ("America/Toronto", "Toronto"),
                            ("Asia/Aqtobe", "Aqtobe"),
                            ("America/Cayman", "Cayman"),
                            ("America/Kentucky/Monticello", "Monticello"),
                            ("America/Kralendijk", "Kralendijk"),
                            ("Pacific/Funafuti", "Funafuti"),
                            ("America/Argentina/Rio_Gallegos", "Rio_Gallegos"),
                            ("Africa/Malabo", "Malabo"),
                            ("America/Indiana/Knox", "Knox"),
                            ("Australia/Hobart", "Hobart"),
                            ("Pacific/Fakaofo", "Fakaofo"),
                            ("America/Cancun", "Cancun"),
                            ("Europe/Skopje", "Skopje"),
                            ("Europe/Jersey", "Jersey"),
                            ("America/Menominee", "Menominee"),
                            ("America/St_Lucia", "St_Lucia"),
                            ("Asia/Samarkand", "Samarkand"),
                            ("America/Indiana/Vevay", "Vevay"),
                            ("Pacific/Noumea", "Noumea"),
                            ("GMT", "GMT"),
                            ("Africa/Mogadishu", "Mogadishu"),
                            ("Africa/Windhoek", "Windhoek"),
                            ("Asia/Gaza", "Gaza"),
                            ("America/Argentina/Buenos_Aires", "Buenos_Aires"),
                            ("Europe/Malta", "Malta"),
                            ("America/Scoresbysund", "Scoresbysund"),
                            ("Pacific/Enderbury", "Enderbury"),
                            ("Asia/Baghdad", "Baghdad"),
                            ("Atlantic/South_Georgia", "South_Georgia"),
                            ("Asia/Oral", "Oral"),
                            ("Europe/Ljubljana", "Ljubljana"),
                            ("Africa/Addis_Ababa", "Addis_Ababa"),
                            ("America/Mazatlan", "Mazatlan"),
                            ("Europe/Vilnius", "Vilnius"),
                            ("Pacific/Honolulu", "Honolulu"),
                            ("America/Bahia", "Bahia"),
                            ("Asia/Omsk", "Omsk"),
                            ("Asia/Magadan", "Magadan"),
                            ("Africa/Banjul", "Banjul"),
                            ("Pacific/Pago_Pago", "Pago_Pago"),
                            ("America/Anchorage", "Anchorage"),
                            ("Asia/Hovd", "Hovd"),
                            ("Pacific/Kwajalein", "Kwajalein"),
                            ("Africa/Juba", "Juba"),
                            ("America/Guadeloupe", "Guadeloupe"),
                            ("Pacific/Kosrae", "Kosrae"),
                            ("Asia/Kamchatka", "Kamchatka"),
                            ("Europe/Astrakhan", "Astrakhan"),
                            ("Europe/Prague", "Prague"),
                            ("Europe/Tallinn", "Tallinn"),
                            ("America/Argentina/Mendoza", "Mendoza"),
                            ("Pacific/Efate", "Efate"),
                            ("America/Curacao", "Curacao"),
                            ("Pacific/Pohnpei", "Pohnpei"),
                            ("Europe/Vatican", "Vatican"),
                            ("Europe/Saratov", "Saratov"),
                            ("Pacific/Norfolk", "Norfolk"),
                            ("America/Port-au-Prince", "Port-au-Prince"),
                            ("Pacific/Apia", "Apia"),
                            ("America/St_Vincent", "St_Vincent"),
                            ("Atlantic/Faroe", "Faroe"),
                            ("Pacific/Tarawa", "Tarawa"),
                            ("America/Indiana/Winamac", "Winamac"),
                            ("Asia/Shanghai", "Shanghai"),
                            ("US/Central", "Central"),
                            ("Pacific/Port_Moresby", "Port_Moresby"),
                            ("America/Tegucigalpa", "Tegucigalpa"),
                            ("America/Guyana", "Guyana"),
                            ("Pacific/Easter", "Easter"),
                            ("Antarctica/Palmer", "Palmer"),
                            ("America/Goose_Bay", "Goose_Bay"),
                            ("Pacific/Saipan", "Saipan"),
                            ("Canada/Mountain", "Mountain"),
                            ("UTC", "UTC"),
                            ("Asia/Karachi", "Karachi"),
                            ("America/Indiana/Petersburg", "Petersburg"),
                            ("America/Indiana/Indianapolis", "Indianapolis"),
                            ("Africa/Luanda", "Luanda"),
                            ("Europe/Vaduz", "Vaduz"),
                            ("Europe/Samara", "Samara"),
                            ("Indian/Mauritius", "Mauritius"),
                            ("Europe/Uzhgorod", "Uzhgorod"),
                            ("Indian/Christmas", "Christmas"),
                            ("Antarctica/Casey", "Casey"),
                            ("America/Cuiaba", "Cuiaba"),
                            ("Asia/Colombo", "Colombo"),
                            ("Indian/Mayotte", "Mayotte"),
                            ("America/Belize", "Belize"),
                            ("Asia/Bahrain", "Bahrain"),
                            ("America/Eirunepe", "Eirunepe"),
                            ("Asia/Damascus", "Damascus"),
                            ("America/Rainy_River", "Rainy_River"),
                            ("America/Costa_Rica", "Costa_Rica"),
                            ("Africa/Asmara", "Asmara"),
                            ("America/Sitka", "Sitka"),
                            ("Asia/Taipei", "Taipei"),
                            ("Pacific/Auckland", "Auckland"),
                            ("Asia/Thimphu", "Thimphu"),
                            ("Africa/Lagos", "Lagos"),
                            ("Asia/Bishkek", "Bishkek"),
                            ("America/Puerto_Rico", "Puerto_Rico"),
                            ("America/Merida", "Merida"),
                            ("Asia/Singapore", "Singapore"),
                            ("Asia/Qyzylorda", "Qyzylorda"),
                            ("Indian/Cocos", "Cocos"),
                            ("Asia/Kathmandu", "Kathmandu"),
                            ("Asia/Yakutsk", "Yakutsk"),
                            ("Europe/Zaporozhye", "Zaporozhye"),
                            ("Asia/Aqtau", "Aqtau"),
                            ("Australia/Brisbane", "Brisbane"),
                            ("Europe/Oslo", "Oslo"),
                            ("Africa/Conakry", "Conakry"),
                            ("Asia/Riyadh", "Riyadh"),
                            ("Asia/Tokyo", "Tokyo"),
                            ("America/Cambridge_Bay", "Cambridge_Bay"),
                            ("Asia/Tbilisi", "Tbilisi"),
                            ("Africa/Nouakchott", "Nouakchott"),
                            ("Asia/Kuwait", "Kuwait"),
                            ("Asia/Novokuznetsk", "Novokuznetsk"),
                            ("America/Bahia_Banderas", "Bahia_Banderas"),
                            ("America/Denver", "Denver"),
                            ("America/Havana", "Havana"),
                            ("Asia/Khandyga", "Khandyga"),
                            ("America/Barbados", "Barbados"),
                            ("America/Belem", "Belem"),
                            ("America/Moncton", "Moncton"),
                            ("Africa/Bujumbura", "Bujumbura"),
                            ("Africa/Blantyre", "Blantyre"),
                            ("Indian/Comoro", "Comoro"),
                            ("Atlantic/St_Helena", "St_Helena"),
                            ("Asia/Barnaul", "Barnaul"),
                            ("Asia/Urumqi", "Urumqi"),
                            ("America/Argentina/San_Luis", "San_Luis"),
                            ("Antarctica/Macquarie", "Macquarie"),
                            ("America/Creston", "Creston"),
                            ("America/Whitehorse", "Whitehorse"),
                            ("Africa/Cairo", "Cairo"),
                            ("Europe/Berlin", "Berlin"),
                            ("America/Indiana/Tell_City", "Tell_City"),
                            ("America/North_Dakota/New_Salem", "New_Salem"),
                            ("America/Thule", "Thule"),
                            ("Asia/Yekaterinburg", "Yekaterinburg"),
                            ("America/Argentina/San_Juan", "San_Juan"),
                            ("America/La_Paz", "La_Paz"),
                            ("America/Argentina/Catamarca", "Catamarca"),
                            ("Pacific/Pitcairn", "Pitcairn"),
                            ("Asia/Choibalsan", "Choibalsan"),
                            ("America/Fortaleza", "Fortaleza"),
                            ("America/Mexico_City", "Mexico_City"),
                            ("Antarctica/Mawson", "Mawson"),
                            ("America/Indiana/Vincennes", "Vincennes"),
                            ("America/Caracas", "Caracas"),
                            ("America/Juneau", "Juneau"),
                            ("Atlantic/Stanley", "Stanley"),
                            ("America/St_Barthelemy", "St_Barthelemy"),
                            ("Asia/Kabul", "Kabul"),
                            ("Europe/Kirov", "Kirov"),
                            ("Australia/Perth", "Perth"),
                            ("Pacific/Bougainville", "Bougainville"),
                            ("America/Jamaica", "Jamaica"),
                            ("Australia/Adelaide", "Adelaide"),
                            ("Indian/Kerguelen", "Kerguelen"),
                            ("Atlantic/Madeira", "Madeira"),
                            ("America/Paramaribo", "Paramaribo"),
                            ("Europe/Copenhagen", "Copenhagen"),
                            ("America/North_Dakota/Center", "Center"),
                            ("Europe/Kiev", "Kiev"),
                            ("Asia/Muscat", "Muscat"),
                            ("America/Lower_Princes", "Lower_Princes"),
                            ("America/Maceio", "Maceio"),
                            ("Canada/Pacific", "Pacific"),
                            ("Indian/Mahe", "Mahe"),
                            ("Europe/Brussels", "Brussels"),
                            ("America/Nuuk", "Nuuk"),
                            ("Asia/Tashkent", "Tashkent"),
                            ("Asia/Yangon", "Yangon"),
                            ("Europe/Paris", "Paris"),
                            ("Europe/Zagreb", "Zagreb"),
                            ("Asia/Jerusalem", "Jerusalem"),
                            ("America/Porto_Velho", "Porto_Velho"),
                            ("Asia/Anadyr", "Anadyr"),
                            ("Asia/Novosibirsk", "Novosibirsk"),
                            ("Europe/London", "London"),
                            ("Africa/Gaborone", "Gaborone"),
                            ("America/Metlakatla", "Metlakatla"),
                            ("Africa/Maputo", "Maputo"),
                            ("America/Hermosillo", "Hermosillo"),
                            ("America/Punta_Arenas", "Punta_Arenas"),
                            ("Europe/Minsk", "Minsk"),
                            ("Europe/Chisinau", "Chisinau"),
                            ("Atlantic/Canary", "Canary"),
                            ("America/Nome", "Nome"),
                            ("Europe/Isle_of_Man", "Isle_of_Man"),
                            ("Asia/Kuala_Lumpur", "Kuala_Lumpur"),
                            ("Pacific/Nauru", "Nauru"),
                            ("Africa/Kampala", "Kampala"),
                            ("America/Martinique", "Martinique"),
                            ("America/Panama", "Panama"),
                            ("Europe/Dublin", "Dublin"),
                            ("Africa/Bissau", "Bissau"),
                            ("America/Argentina/La_Rioja", "La_Rioja"),
                            ("America/Kentucky/Louisville", "Louisville"),
                            ("Europe/Rome", "Rome"),
                            ("America/Blanc-Sablon", "Blanc-Sablon"),
                            ("Atlantic/Cape_Verde", "Cape_Verde"),
                            ("Asia/Famagusta", "Famagusta"),
                            ("US/Alaska", "Alaska"),
                            ("Australia/Darwin", "Darwin"),
                            ("America/Winnipeg", "Winnipeg"),
                            ("Europe/Madrid", "Madrid"),
                            ("America/Dominica", "Dominica"),
                            ("Asia/Dushanbe", "Dushanbe"),
                            ("Europe/Monaco", "Monaco"),
                            ("Africa/Nairobi", "Nairobi"),
                            ("Canada/Atlantic", "Atlantic"),
                            ("Pacific/Guadalcanal", "Guadalcanal"),
                            ("America/Argentina/Salta", "Salta"),
                            ("Africa/Algiers", "Algiers"),
                            ("Pacific/Tahiti", "Tahiti"),
                            ("America/Montserrat", "Montserrat"),
                            ("Pacific/Midway", "Midway"),
                            ("Europe/Helsinki", "Helsinki"),
                            ("America/Adak", "Adak"),
                            ("Asia/Atyrau", "Atyrau"),
                            ("America/North_Dakota/Beulah", "Beulah"),
                            ("Europe/Volgograd", "Volgograd"),
                            ("America/New_York", "New_York"),
                            ("Europe/Lisbon", "Lisbon"),
                            ("America/Thunder_Bay", "Thunder_Bay"),
                            ("Europe/Ulyanovsk", "Ulyanovsk"),
                            ("Asia/Vientiane", "Vientiane"),
                            ("Asia/Dubai", "Dubai"),
                            ("America/Tijuana", "Tijuana"),
                            ("Asia/Nicosia", "Nicosia"),
                            ("Asia/Pyongyang", "Pyongyang"),
                            ("America/Argentina/Cordoba", "Cordoba"),
                            ("America/Asuncion", "Asuncion"),
                            ("America/Anguilla", "Anguilla"),
                            ("Africa/Ceuta", "Ceuta"),
                            ("Australia/Lord_Howe", "Lord_Howe"),
                            ("America/Port_of_Spain", "Port_of_Spain"),
                            ("Asia/Ho_Chi_Minh", "Ho_Chi_Minh"),
                            ("Africa/Accra", "Accra"),
                            ("America/Nipigon", "Nipigon"),
                            ("Africa/Libreville", "Libreville"),
                            ("America/Edmonton", "Edmonton"),
                            ("Africa/Kigali", "Kigali"),
                            ("America/Matamoros", "Matamoros"),
                            ("Asia/Srednekolymsk", "Srednekolymsk"),
                            ("Indian/Antananarivo", "Antananarivo"),
                            ("Asia/Irkutsk", "Irkutsk"),
                            ("Pacific/Chuuk", "Chuuk"),
                            ("America/Marigot", "Marigot"),
                            ("America/Guayaquil", "Guayaquil"),
                            ("Africa/Abidjan", "Abidjan"),
                            ("Europe/Kaliningrad", "Kaliningrad"),
                            ("Europe/Amsterdam", "Amsterdam"),
                            ("Pacific/Marquesas", "Marquesas"),
                            ("Pacific/Galapagos", "Galapagos"),
                            ("Pacific/Gambier", "Gambier"),
                            ("Europe/Warsaw", "Warsaw"),
                            ("Africa/Tunis", "Tunis"),
                            ("Pacific/Guam", "Guam"),
                            ("America/Santiago", "Santiago"),
                            ("Africa/Bamako", "Bamako"),
                            ("Europe/Tirane", "Tirane"),
                            ("Arctic/Longyearbyen", "Longyearbyen"),
                            ("Europe/Bucharest", "Bucharest"),
                            ("Africa/Maseru", "Maseru"),
                            ("Pacific/Tongatapu", "Tongatapu"),
                            ("America/Santo_Domingo", "Santo_Domingo"),
                            ("Asia/Macau", "Macau"),
                            ("Pacific/Fiji", "Fiji"),
                            ("America/Noronha", "Noronha"),
                            ("Asia/Brunei", "Brunei"),
                            ("Europe/Belgrade", "Belgrade"),
                            ("US/Hawaii", "Hawaii"),
                            ("America/Santarem", "Santarem"),
                            ("Europe/Sarajevo", "Sarajevo"),
                            ("Africa/Harare", "Harare"),
                            ("America/St_Thomas", "St_Thomas"),
                            ("America/El_Salvador", "El_Salvador"),
                            ("Africa/Ndjamena", "Ndjamena"),
                            ("Asia/Kolkata", "Kolkata"),
                            ("Canada/Newfoundland", "Newfoundland"),
                            ("Europe/Stockholm", "Stockholm"),
                            ("America/Argentina/Jujuy", "Jujuy"),
                            ("America/Lima", "Lima"),
                            ("Asia/Aden", "Aden"),
                            ("Africa/Kinshasa", "Kinshasa"),
                            ("Africa/Douala", "Douala"),
                            ("Africa/Monrovia", "Monrovia"),
                            ("Pacific/Wallis", "Wallis"),
                            ("America/Boise", "Boise"),
                            ("America/Fort_Nelson", "Fort_Nelson"),
                            ("America/Montevideo", "Montevideo"),
                            ("America/Recife", "Recife"),
                            ("Asia/Jayapura", "Jayapura"),
                            ("Asia/Chita", "Chita"),
                            ("Asia/Bangkok", "Bangkok"),
                            ("Antarctica/Vostok", "Vostok"),
                            ("Australia/Sydney", "Sydney"),
                        ],
                        default="America/Puerto_Rico",
                        max_length=255,
                        verbose_name="user's timezone",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
            managers=[
                ("objects", una_hora.users.models.CustomUserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["email"], name="users_user_email_6f2530_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(
                fields=["-date_joined"], name="users_user_date_jo_5abcb7_idx"
            ),
        ),
    ]
