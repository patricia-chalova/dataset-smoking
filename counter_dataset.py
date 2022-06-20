import random
from datetime import datetime as dt
import datetime
import numpy as np
import pandas as pd


# core demographics and values
def core(type1, type1_perc, type2, type2_perc, size):

    gender = ''
    occupation = ''
    education = ''
    country = ''
    city = ''
    entry_type = ''
    age = ''
    yos = ''
    noc = ''
    tp_of_prdct = ''
    fc = ''
    fc_year = ''
    fc_like = ''
    ttq = ''
    ttq_nums = ''
    mthd_1 = ''
    mthd_2 = ''
    mthd_3 = ''
    mthd_4 = ''
    mthd_5 = ''
    mthd_6 = ''
    fail_rsn = ''
    hlth_iss = ''
    start_smoking = ''
    cs = ''
    lc_date = ''
    lc_signif = ''
    lc_signif_desc = ''
    win_mthd = ''
    qt_rsn = ''
    nw_hbt = ''
    nw_hbt_desc = ''
    gn_wght = ''
    urg_smoke = ''
    urg_smoke_num = ''
    urg_smoke_num_tf = ''
    urg_smoke_desc = ''
    ns_tried = ''
    ns_tried_age = ''
    ns_no_start = ''
    smoker = ''

    size1 = int(type1_perc * (size/100))
    size2 = int(type2_perc * (size/100))
    min_age = 16
    df_list = []
    dict_dem = {}
    dict_smok = {}
    dict_non_s = {}

    def demo(size):
        gender = np.random.choice(['F', 'M', 'O'], p=[0.48, 0.48, 0.04])
        occupation = random.choice(['IT', 'Agriculture', 'Finance', 'Health Services', 'Education Services',
                                    'Manufacturing', 'Retail', 'Hospitality'])
        education = random.choice(
            ['High School', 'Associate Degree', 'Bachelor Degree', 'Master\'s Degree', 'Doctoral Degree'])
        country = random.choice(
            ['USA', 'CA', 'MX', 'FR', 'UK', 'DE', 'IT', 'CN', 'AU', 'NZ', 'RU', 'PL', 'BR', 'IN', 'JP'])
        city = ''
        if country == 'USA':
            city = random.choice(['New York City', 'Boston', 'Miami', 'Los Angeles'])
        elif country == 'CA':
            city = random.choice(['Vancouver', 'Toronto', 'Montreal'])
        elif country == 'MX':
            city = random.choice(['Mexico City', 'Tijuana', 'Ecatepec'])
        elif country == 'FR':
            city = random.choice(['Paris', 'Lyon', 'Nice'])
        elif country == 'UK':
            city = random.choice(['London', 'Manchester', 'Birmingham'])
        elif country == 'DE':
            city = random.choice(['Berlin', 'Munich', 'Hamburg'])
        elif country == 'IT':
            city = random.choice(['Rome', 'Milan', 'Florence'])
        elif country == 'CN':
            city = random.choice(['Beijing', 'Shenzhen', 'Shanghai'])
        elif country == 'AU':
            city = random.choice(['Sydney', 'Perth', 'Melbourne'])
        elif country == 'NZ':
            city = random.choice(['Auckland', 'Wellington', 'Hamilton'])
        elif country == 'RU':
            city = random.choice(['Moscow', 'Saint Petersburg', 'Novosibirsk'])
        elif country == 'PL':
            city = random.choice(['Warsaw', 'Krakow', 'Gdansk'])
        elif country == 'BR':
            city = random.choice(['Rie de Janeiro', 'Sao Paulo', 'Fortaleza'])
        elif country == 'IN':
            city = random.choice(['Mumbai', 'Bangalore', 'Hyderabad'])
        elif country == 'JP':
            city = random.choice(['Tokyo', 'Osaka', 'Yokohama'])

        entry_type = 'F'

        dict_dem = {'gender': gender, 'occupation': occupation, 'education': education, 'country': country, 'city': city,
                    'entry_type': entry_type}
        return dict_dem

    for i in range(1, size1):
        age = ''
        yos = ''
        noc = ''
        tp_of_prdct = ''
        fc = ''
        fc_year = ''
        fc_like = ''
        ttq = ''
        ttq_nums = ''
        mthd_1 = ''
        mthd_2 = ''
        mthd_3 = ''
        mthd_4 = ''
        mthd_5 = ''
        mthd_6 = ''
        fail_rsn = ''
        hlth_iss = ''
        start_smoking = ''
        cs = ''
        lc_date = ''
        lc_signif = ''
        lc_signif_desc = ''
        win_mthd = ''
        qt_rsn = ''
        nw_hbt = ''
        nw_hbt_desc = ''
        gn_wght = ''
        urg_smoke = ''
        urg_smoke_num = ''
        urg_smoke_num_tf = ''
        urg_smoke_desc = ''
        ns_tried = ''
        ns_tried_age = ''
        ns_no_start = ''

        demo_dict = demo(size1)

        age = random.randint(16, 76)
        yos = 0
        if age - min_age == 0:
            yos = 0
        else:
            yos = random.randint(1, age - min_age)

        noc = random.randint(1, 40)
        tp_of_prdct = random.choice(['Cigarettes', 'Vaping product', 'Cigars', 'Smokeless product'])
        fc_x = ''
        if age - yos > 26:
            fc_x = 26
        else:
            fc_x = age - yos

        fc = random.randint(13, fc_x)
        fc_year = dt.now().year - (age - fc)
        fc_like = np.random.choice(['yes', 'no'], p=[0.3, 0.7])
        ttq = random.choice(['yes', 'no'])
        if ttq == 'yes':
            ttq_nums = random.randint(1, 7)
            mthd_list = []
            for i in range(1, ttq_nums +1):
                mthd = np.random.choice(['Cold Turkey', 'Gradual Reduction', 'Nicotine Replacement Therapy',
                                         'Medication', 'Hypnosis', 'Other'], p=[0.25, 0.25, 0.25, 0.15, 0.05, 0.05])
                mthd_list.append(mthd)

            mthd_1 = mthd_list[0]

            try:
                mthd_2 = mthd_list[1]

                try:
                    mthd_3 = mthd_list[2]

                    try:
                        mthd_4 = mthd_list[3]

                        try:
                            mthd_5 = mthd_list[4]

                            try:
                                mthd_6 = mthd_list[5]

                            except:
                                pass
                        except:
                            pass
                    except:
                        pass

                except:
                    pass

            except:
                pass

            fail_rsn = random.choice(['Stress', 'Family', 'Withdrawal Symptoms', 'Other'])

        hlth_iss = random.choice(['yes', 'no'])
        start_smoking=  random.choice(['Friends', 'Family', 'Other'])
        cs = random.choice(['yes', 'no'])
        if cs == 'no':
            start_age = random.randint(fc, (age - yos))
            start_year = dt.now().year - (age - start_age)
            lc = start_age + yos
            rand_month = random.randint(1,12)
            rand_day = 0
            if rand_month in [1, 3, 5, 7, 8, 10, 12]:
                rand_day = random.randint(1, 31)
            else:
                rand_day = random.randint(1, 30)

            if rand_month == 2:
                rand_day = random.randint(1, 28)
            lc_date = datetime.datetime(start_year + yos, rand_month, rand_day)
            lc_signif = random.choice(['yes', 'no'])
            if lc_signif == 'yes':
                if lc_date.month == 1 and lc_date.day == 1:
                    lc_signif_desc = 'New Year\'s Resolution'
                else:
                    lc_signif_desc = random.choice(['Birthday', 'Anniversary', 'Other'])

            win_mthd = np.random.choice(['Cold Turkey', 'Gradual Reduction', 'Nicotine Replacement Therapy',
                                         'Medication', 'Hypnosis', 'Other'], p=[0.25, 0.25, 0.25, 0.15, 0.05, 0.05])
            nw_hbt = random.choice(['yes', 'no'])
            if nw_hbt == 'yes':
                nw_hbt_desc = random.choice(['Chewing gum', 'Beverage', 'Snack', 'Physical activity', 'Other'])

            if hlth_iss == 'yes':
                qt_rsn = 'Health issues'
            else:
                qt_rsn = random.choice(['Family', 'Friends', 'General health', 'Dislike', 'Other'])

            gn_wght = random.choice(['yes', 'no'])
            urg_smoke = random.choice(['yes', 'no'])

            if urg_smoke == 'yes':
                urg_smoke_num = random.randint(1, 11)
                urg_smoke_num_tf = random.choice(['Day', 'Week', 'Month', 'Year'])
                urg_smoke_desc = random.choice(['Party', 'Smell', 'Drinking', 'Seeing someone smoking', 'Other'])

        dict_smok = {'age': age, 'yos': yos, 'cs': cs, 'noc': noc, 'tp_of_prdct': tp_of_prdct, 'fc': fc, 'fc_year': fc_year,
                     'fc_like': fc_like, 'start_smoking': start_smoking, 'lc_date': str(lc_date), 'lc_signif': lc_signif,
                     'lc_signif_desc': lc_signif_desc, 'ttq': ttq,
                     'ttq_nums': ttq_nums, 'mthd_1': mthd_1, 'mthd_2': mthd_2, 'mthd_3': mthd_3, 'mthd_4': mthd_4, 'mthd_5': mthd_5,
                     'mthd_6': mthd_6, 'fail_rsn':fail_rsn, 'win_mthd': win_mthd, 'nw_hbt': nw_hbt, 'nw_hbt_desc':nw_hbt_desc,
                     'qt_rsn': qt_rsn, 'hlth_iss': hlth_iss, 'gn_wght': gn_wght, 'urg_smoke': urg_smoke,
                     'urg_smoke_num': urg_smoke_num, 'urg_smoke_num_tf': urg_smoke_num_tf, 'urg_smoke_desc': urg_smoke_desc,
                     'ns_tried': ns_tried, 'ns_tried_age': ns_tried_age, 'ns_no_start': ns_no_start, 'smoker': 'yes'}
        dict_inter = []
        dict_inter.extend([dict_smok, demo_dict])


        x = {k: v for x in dict_inter for k, v in x.items()}
        df_list.append(x)

    for i in range(1, size2):
        age = ''
        yos = ''
        noc = ''
        tp_of_prdct = ''
        fc = ''
        fc_year = ''
        fc_like = ''
        ttq = ''
        ttq_nums = ''
        mthd_1 = ''
        mthd_2 = ''
        mthd_3 = ''
        mthd_4 = ''
        mthd_5 = ''
        mthd_6 = ''
        fail_rsn = ''
        hlth_iss = ''
        start_smoking = ''
        cs = ''
        lc_date = ''
        lc_signif = ''
        lc_signif_desc = ''
        win_mthd = ''
        qt_rsn = ''
        nw_hbt = ''
        nw_hbt_desc = ''
        gn_wght = ''
        urg_smoke = ''
        urg_smoke_num = ''
        urg_smoke_num_tf = ''
        urg_smoke_desc = ''
        ns_tried = ''
        ns_tried_age = ''
        ns_no_start = ''

        dict_dem2 = demo(size2)
        age = random.randint(16, 76)
        ns_tried = random.choice(['yes', 'no'])

        if ns_tried == 'yes':
            ns_tried_age = random.randint(13, 26)
            fc_like = random.choice(['yes', 'no'])
            if fc_like == 'yes':
                ns_no_start = 'Didn\'t like it'
            else:
                ns_no_start = random.choice(['Didn\'t like it', 'No friends smoking', 'Other'])

        dict_non_s = {'age': age, 'yos': yos, 'cs': cs, 'noc': noc, 'tp_of_prdct': tp_of_prdct, 'fc': fc, 'fc_year': fc_year,
                     'fc_like': fc_like, 'start_smoking': start_smoking, 'lc_date': str(lc_date), 'lc_signif': lc_signif,
                     'lc_signif_desc': lc_signif_desc, 'ttq': ttq,
                     'ttq_nums': ttq_nums, 'mthd_1': mthd_1, 'mthd_2': mthd_2, 'mthd_3': mthd_3, 'mthd_4': mthd_4, 'mthd_5': mthd_5,
                     'mthd_6': mthd_6, 'fail_rsn':fail_rsn, 'win_mthd': win_mthd, 'nw_hbt': nw_hbt, 'nw_hbt_desc':nw_hbt_desc,
                     'qt_rsn': qt_rsn, 'hlth_iss': hlth_iss, 'gn_wght': gn_wght, 'urg_smoke': urg_smoke,
                     'urg_smoke_num': urg_smoke_num, 'urg_smoke_num_tf': urg_smoke_num_tf, 'urg_smoke_desc': urg_smoke_desc,
                     'ns_tried': ns_tried, 'ns_tried_age': ns_tried_age, 'ns_no_start': ns_no_start, 'smoker': 'no'}

        dict_inter2 = []
        dict_inter2.extend([dict_non_s, dict_dem2])


        x = {k: v for x in dict_inter2 for k, v in x.items()}
        df_list.append(x)


    df = pd.DataFrame(df_list)
    df.to_csv('smoking_test.csv', index=False)


core('smoker', 80, 'non-smoker', 20, 1000)

