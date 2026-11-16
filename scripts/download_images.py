import os
import requests
import json

os.makedirs('images', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0'}

image_map = {
    "logo.png": "https://image.makewebcdn.com/makeweb/m_200x200/LFlha9Qld/DefaultData/67EEEC86_8D87_4A7B_BDB0_869EE700FDEA.jpeg?v=202405291424",
    "hero-banner.jpg": "https://image.makewebeasy.net/makeweb/m_1920x0/LFlha9Qld/DefaultData/264E675E_7E20_45DE_A530_A24FAFC02074.jpeg?v=202012190947",
    "line-divider.png": "https://image.makewebeasy.net/mwetemplate/0/template0145/DefaultData/t144_line.png?v=202012190947",
    "srv-inbound.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/EF6B6B7D_3872_47F6_8B14_254BCC2367A5.jpeg?v=202405291424",
    "srv-outbound.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/22D0EECA_1914_4980_A03F_B5E21DED8CC2.jpeg?v=202405291424",
    "srv-social.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/6BB84738_C375_4A3E_8138_61CC623661B6.jpeg?v=202405291424",
    "srv-onsite.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/3C65F981_B184_4862_8DD1_9CF988F1283B.jpeg?v=202405291424",
    "srv-spot-ads.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/Capture_5.jpg?v=202405291424",
    "srv-tv-air.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/S__19300357.jpg?v=202405291424",
    "srv-cloud-pbx.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/S__19300359.jpg?v=202405291424",
    "cap-outsource.jpg": "https://image.makewebcdn.com/makeweb/m_1920x0/LFlha9Qld/DefaultData%2FB763BB18_7AFF_4A4E_A2E3_EC42CE3E1379.jpeg?v=202405291424",
    "cap-pbx.jpg": "https://image.makewebcdn.com/makeweb/m_1920x0/LFlha9Qld/DefaultData%2FS__19300354.jpg?v=202405291424",
    "cap-tv.jpg": "https://image.makewebcdn.com/makeweb/m_1920x0/LFlha9Qld/DefaultData%2FS__19300356.jpg?v=202405291424",
    "cap-import-export.jpg": "https://image.makewebcdn.com/makeweb/m_1920x0/LFlha9Qld/DefaultData%2F12511CA9_2878_4226_A143_8AD350CE8A61.jpeg?v=202405291424",
    "cap-data-analysis.jpg": "https://image.makewebcdn.com/makeweb/m_1920x0/LFlha9Qld/DefaultData%2FDE7E1508_D602_4EE6_98DA_4EB6B0788E46.jpeg?v=202405291424",
    "cap-fulfillment.jpg": "https://image.makewebcdn.com/makeweb/m_1920x0/LFlha9Qld/DefaultData%2FE1D66C8E_46BE_4DC6_A442_D9751725AFD6.jpeg?v=202405291424",
    "client-logos.jpg": "https://image.makewebcdn.com/makeweb/0/LFlha9Qld/DefaultData/1428E9A4_C66A_4077_9137_2EE2E4477745.jpeg?v=202405291424",
    "award-1668.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/068EDF16_8E7E_4466_91F8_AED9EF9B9923.jpeg?v=202405291424",
    "award-tccta-gold.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/7D092F7A_2855_400F_A13C_ED7663AEE8D9.jpeg?v=202405291424",
    "award-tccta-covid.jpg": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/7B54C6A1_A5E8_4D63_A76C_B9F93F7EE5B1.jpeg?v=202405291424",
    "atmosphere.gif": "https://image.makewebcdn.com/makeweb/m_750x0/LFlha9Qld/DefaultData/19A74C8D_A839_4D54_A34D_A3ED44165CEA.gif?v=202405291424",
    "dhipaya-training.png": "https://image.makewebeasy.net/makeweb/0/LFlha9Qld/DefaultData/AW_เว็ปศูนย์ฝึก.png?v=202305101549"
}

for fname, url in image_map.items():
    fpath = os.path.join('images', fname)
    if not os.path.exists(fpath):
        try:
            r = requests.get(url, headers=headers, timeout=15)
            if r.status_code == 200:
                with open(fpath, 'wb') as f:
                    f.write(r.content)
                print(f"Downloaded {fname} ({len(r.content)} bytes)")
            else:
                print(f"Failed {fname}: {r.status_code}")
        except Exception as e:
            print(f"Error {fname}: {e}")
    else:
        print(f"Already exists: {fname}")

print("Image download check finished.")
