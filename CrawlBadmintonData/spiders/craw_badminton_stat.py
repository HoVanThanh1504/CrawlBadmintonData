import scrapy
import requests
from random import randint

# Define ScrapeOps API key
SCRAPEOPS_API_KEY = '0ce1de82-a69f-41bc-9a2f-bb30cacea198'


# Function to get a list of user agents from ScrapeOps
def get_user_agent_list():
    response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + SCRAPEOPS_API_KEY)
    json_response = response.json()
    return json_response.get('result', [])


# Function to get a random user agent from the list
def get_random_user_agent(user_agent_list):
    random_index = randint(0, len(user_agent_list) - 1)
    return user_agent_list[random_index]


# Retrieve User-Agent List From ScrapeOps
user_agent_list = get_user_agent_list()
print(len(user_agent_list))

class CrawBadmintonStatSpider(scrapy.Spider):
    name = "craw_badminton_stat"
    allowed_domains = ["bwfbadminton.com"]
    # List of URLs to start scraping from
    start_urls = ['https://bwfworldtour.bwfbadminton.com/tournament/4036/daihatsu-indonesia-masters-2021-new-dates/results/2021-11-16',
                'https://bwfworldtour.bwfbadminton.com/tournament/3351/perodua-malaysia-masters-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3388/daihatsu-indonesia-masters-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3376/yonex-all-england-open-badminton-championships-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3392/yonex-sunrise-india-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3355/celcom-axiata-malaysia-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3356/singapore-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3394/blibli-indonesia-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3359/daihatsu-yonex-japan-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3360/toyota-thailand-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3364/victor-china-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3365/korea-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3367/danisa-denmark-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3368/yonex-french-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3519/fuzhou-china-open-2019/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3687/perodua-malaysia-masters-2020/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3752/daihatsu-indonesia-masters-2020/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3690/yonex-all-england-open-2020/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3801/danisa-denmark-open-i-2020/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4108/yonex-thailand-open/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4109/toyota-thailand-open/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3982/yonex-all-england-open-badminton-championships-2021/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3971/victor-denmark-open-2021/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3972/yonex-french-open-2021/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/3979/hylo-open-2021-formerly-saarlorlux-open/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4036/daihatsu-indonesia-masters-2021-new-dates/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4039/siminvest-indonesia-open-2021-new-dates/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4426/yonex-sunrise-india-open-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4431/yonex-all-england-open-badminton-championships-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4434/korea-open-badminton-championships-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4436/gr-toyota-gazoo-racing-thailand-open-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4436/gr-toyota-gazoo-racing-thailand-open-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4438/east-ventures-indonesia-open-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4439/petronas-malaysia-open-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4440/perodua-malaysia-masters-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4441/singapore-open-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4444/daihatsu-yonex-japan-open-2022/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4475/denmark-open-2022-presented-by-victor/results/podium/',
                'https://bwfworldtour.bwfbadminton.com/tournament/4446/yonex-french-open-2022/results/podium/',
                ]

    def parse(self, response):
        """
        go through all tournament day
        :param resposne:
        :return:
        """
        for link in response.css('#ajaxTabsResults a'):
            if link.css('a::text').get().strip() not in ['PODIUM', 'DRAWS']:
                # Follow the link and call the 'parse1' function with a random user agent
                yield response.follow(link.css('a::attr(href)').get(), callback=self.parse1,
                                      headers={'User-Agent': get_random_user_agent(user_agent_list)})

    def parse1(self, response):
        """
        go through statistic link of each pair
        :param response:
        :return:
        """
        # Iterate through links to individual match statistics
        for link in response.xpath('//*[@id="match-link"]/@href'):
            unique_dict = {}
            link = link.get().replace("stab=result", "stab=match")
            # Follow the link and call the 'parse_info' function with a random user agent
            yield response.follow(link, callback=self.parse_info, meta={'unique_dict': unique_dict},
                                  headers={'User-Agent': get_random_user_agent(user_agent_list)})

    def parse_info(self, response):
        # Parse individual match statistics
        unique_key = response.url.split("&")[0]
        unique_dict = response.meta['unique_dict']

        # Extract relevant information from the page
        return_dict = {
            'T': response.xpath('//*[@id="tab-content1"]/h3/text()').get().split(" ")[-2],
            'MatchScore': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[10]/td[2]/text()').get(),
            'P1/T1-TP': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[9]/td[1]/text()').get(),
            'P2/T2-TP': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[9]/td[3]/text()').get(),
            'P1/T1-L': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[9]/td[3]/text()').get(),
            'P2/T2-L': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[9]/td[1]/text()').get(),
            'P1/T1-W': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[10]/td[1]/div/text()').get(),
            'P2/T2-W': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[10]/td[3]/div/text()').get(),
            'P1/T1-GP': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[2]/td[1]/text()').get().strip(),
            'P2/T2-GP': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[2]/td[3]/text()').get().strip(),
            'P1/T1-LP': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[1]/td[1]/text()').get().strip(),
            'P2/T2-LP': response.xpath('//*[@id="tab-content1"]/div/div/table/tr[1]/td[3]/text()').get().strip(),
            }
        for key, value in return_dict.items():
            if unique_key not in unique_dict:
                unique_dict[unique_key] = {'Y': response.xpath('//*[@id="wrapper-background"]/section[3]/div/div/div/div/div[2]/div/h3/text()').get().strip()[-4:], key: value}
            else:
                unique_dict[unique_key][key] = value
                link = response.url.replace("stab=match", "stab=h2h")
                yield response.follow(link, meta={'unique_dict': unique_dict}, callback=self.parse_other_info,
                                      headers={'User-Agent': get_random_user_agent(user_agent_list)})

    def parse_other_info(self, response):
        unique_key = response.url.split("&")[0]
        unique_dict = response.meta['unique_dict']
        seed = response.xpath('//*[@id="wrapper-background"]/section[3]/div/div/div/div/div[2]/div/div/ul/li[contains(@class, "active")]')
        p1t1_s = seed.css('#match-link > div.player-score-wrap > div.player-wrap > div:nth-child(1) > div > div.player1.player_winner ::text').get()
        if "[" in p1t1_s:
            p1t1_s = p1t1_s.split("[")
            p1t1_s = p1t1_s[1][0]
        else:
            p1t1_s = 0
        p2t2_s = seed.css('#match-link > div.player-score-wrap > div.player-wrap > div:nth-child(3) > div > div.player3 ::text').get()
        if "[" in p2t2_s:
            p2t2_s = p2t2_s.split("[")
            p2t2_s = p2t2_s[1][0]
        else:
            p2t2_s = 0

        if len(response.xpath('//*[@id="tab-content4"]/div/div[1]/div[3]/div/div[2]/div[2]/a').getall()) == 2:
            return_dict = {
                'P1': None,
                'P1-C': None,
                'P1T1': response.xpath('//*[@id="tab-content4"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/a/text()').get().strip(), # GET in h2h
                'P1T1-C': response.css('#tab-content4 > div > div.live-profile-row > div:nth-child(1) > div:nth-child(1) > div.player1-info > div.player1-flag > img ::attr(title)').get(), # GET in h2h
                'P2T1': response.xpath('//*[@id="tab-content4"]/div/div[1]/div[1]/div[2]/div[1]/div[2]/a/text()').get().strip(), # GET in h2h
                'P2T1-C': response.css('#tab-content4 > div > div.live-profile-row > div:nth-child(1) > div:nth-child(1) > div.player1-info > div.player1-flag > img ::attr(title)').get(), # GET in h2h
                'P1/T1-S': p1t1_s,
                'P2': None,
                'P2-C': None,
                'P1T2': response.xpath('//*[@id="tab-content4"]/div/div[1]/div[3]/div[1]/div[2]/div[2]/a/text()').get().strip(), # GET in h2h
                'P1T2-C': response.css('#tab-content4 > div > div.live-profile-row > div:nth-child(3) > div:nth-child(1) > div.player2-info > div.player2-flag > img ::attr(title)').get(), # GET in h2h
                'P2T2': response.xpath('//*[@id="tab-content4"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/a/text()').get().strip(), # GET in h2h
                'P2T2-C': response.css('#tab-content4 > div > div.live-profile-row > div:nth-child(3) > div:nth-child(1) > div.player2-info > div.player2-flag > img ::attr(title)').get(), # GET in h2h
                'P2/T2-S': p2t2_s,
                'P1-H2H': response.xpath('//*[@id="tab-content4"]/div/div[2]/div[1]/text()').get().strip(),
                'P2-H2H': response.xpath('//*[@id="tab-content4"]/div/div[2]/div[3]/text()').get().strip()
                }
            for key, value in return_dict.items():
                if unique_key not in response.meta['unique_dict']:
                    response.meta['unique_dict'][unique_key] = {key: value}
                else:
                    response.meta['unique_dict'][unique_key][key] = value
        else:
            return_dict = {
                'P1': response.xpath('//*[@id="tab-content4"]/div/div[1]/div[1]/div/div[1]/div[2]/a/text()').get().strip(),
                'P1-C': response.css('#tab-content4 > div > div.live-profile-row > div:nth-child(1) > div > div.player1-info > div.player1-flag > img ::attr(title)').get(),        'P1T1': None,
                'P1T1-C': None,
                'P2T1': None,
                'P2T1-C': None,
                'P1/T1-S': p1t1_s,
                'P2': response.xpath('//*[@id="tab-content4"]/div/div[1]/div[3]/div/div[2]/div[2]/a/text()').get().strip(), # GET in h2h
                'P2-C': response.css('#tab-content4 > div > div.live-profile-row > div:nth-child(3) > div > div.player2-info > div.player2-flag > img ::attr(title)').get(),
                'P1T2': None,
                'P1T2-C': None,
                'P2T2': None,
                'P2T2-C': None,
                'P2/T2-S': p2t2_s,
                'P1-H2H': response.xpath('//*[@id="tab-content4"]/div/div[2]/div[1]/text()').get().strip(),
                'P2-H2H': response.xpath('//*[@id="tab-content4"]/div/div[2]/div[3]/text()').get().strip()
                }
            for key, value in return_dict.items():
                if unique_key not in unique_dict:
                    unique_dict[unique_key] = {key: value}
                else:
                    unique_dict[unique_key][key] = value
        yield unique_dict
