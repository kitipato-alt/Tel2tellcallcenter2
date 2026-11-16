import os

# 1. OUTBOUND PAGE
outbound_html = """<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Outbound Call Center & Telesales | Tel2Tell Call Center</title>
  <link rel="icon" type="image/png" href="images/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Prompt:wght@300;400;500;600;700&family=Sarabun:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: { navy: '#1B2A38', dark: '#111923', card: '#223446', cyan: '#0EA5E9', accent: '#22D3EE', gold: '#F59E0B' }
          },
          fontFamily: { prompt: ['Prompt', 'sans-serif'], sarabun: ['Sarabun', 'sans-serif'] }
        }
      }
    }
  </script>
</head>
<body class="bg-slate-50 text-slate-800 font-['Prompt','Sarabun'] antialiased">
  <!-- Nav -->
  <header class="sticky top-0 z-50 bg-[#1B2A38]/90 backdrop-blur border-b border-slate-700">
    <div class="max-w-7xl mx-auto px-4 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3">
        <img src="images/logo.png" alt="Tel2Tell" class="h-10 w-auto bg-white/90 p-1 rounded-lg">
        <span class="text-xl font-bold text-white font-['Prompt']">TEL2TELL</span>
      </a>
      <nav class="hidden md:flex items-center gap-6 text-sm text-slate-200">
        <a href="index.html" class="hover:text-brand-accent">หน้าแรก</a>
        <a href="outbound.html" class="text-brand-accent font-bold">Outbound Callcenter</a>
        <a href="sales-admin.html" class="hover:text-brand-accent">Sales Admin</a>
        <a href="vdo-production.html" class="hover:text-brand-accent">VDO Production</a>
        <a href="jobs.html" class="text-brand-gold font-semibold">รับสมัครงาน</a>
        <a href="index.html#contact" class="px-4 py-2 bg-brand-cyan text-white rounded-lg font-bold">ติดต่อเรา</a>
      </nav>
    </div>
  </header>

  <!-- Hero Outbound -->
  <section class="bg-gradient-to-br from-brand-dark via-brand-navy to-slate-900 text-white py-20 border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7 space-y-6">
        <span class="px-3 py-1 bg-amber-500/20 border border-amber-500/30 text-brand-gold text-xs font-bold rounded-full">
          OUTBOUND SALES ADMIN SERVICE
        </span>
        <h1 class="text-3xl sm:text-5xl font-extrabold leading-tight">
          เปลี่ยนทุกสายโทรศัพท์เป็นยอดขาย สร้างความสัมพันธ์ลูกค้ายั่งยืน
        </h1>
        <p class="text-slate-300 text-base font-['Sarabun'] leading-relaxed">
          ในยุคที่การแข่งขันดุเดือด การโทรออกเชิงรุกและการดูแลลูกค้าอย่างใกล้ชิดด้วยทีม Telesales มืออาชีพ พร้อมระบบ CRM อัจฉริยะ จะช่วยให้คุณไม่พลาดทุกโอกาสทางธุรกิจ และสร้างยอดขายเติบโตอย่างต่อเนื่อง
        </p>
        <div class="flex gap-4 pt-2">
          <a href="index.html#contact" class="px-7 py-3.5 bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold rounded-xl shadow-lg shadow-cyan-500/20 transition">
            ขอคำปรึกษาแพ็กเกจ Telesales
          </a>
          <a href="tel:0890404627" class="px-6 py-3.5 bg-slate-800 hover:bg-slate-700 text-white font-semibold rounded-xl border border-slate-700 flex items-center gap-2">
            <i class="fa-solid fa-phone"></i> 089-040-4627
          </a>
        </div>
      </div>
      <div class="lg:col-span-5">
        <img src="images/srv-outbound.jpg" alt="Outbound Call Center" class="rounded-2xl shadow-2xl border border-slate-700">
      </div>
    </div>
  </section>

  <!-- Key Features -->
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 space-y-12">
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <h2 class="text-3xl font-extrabold text-brand-navy">จุดเด่นบริการ Outbound Call Center</h2>
        <p class="text-slate-600 text-sm font-['Sarabun']">เทคโนโลยีทันสมัย ผสานทีมงานมืออาชีพที่มี Service Mind</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
          <div class="w-12 h-12 bg-cyan-100 text-brand-cyan rounded-xl flex items-center justify-center font-bold text-xl"><i class="fa-solid fa-laptop-code"></i></div>
          <h3 class="font-bold text-brand-navy">ระบบ CRM อัจฉริยะ</h3>
          <p class="text-xs text-slate-600 font-['Sarabun'] leading-relaxed">บันทึกผลการติดต่อทุกเคสอย่างละเอียด ติดตามประวัติและสถานะลูกค้าได้อย่างแม่นยำ</p>
        </div>
        <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
          <div class="w-12 h-12 bg-amber-100 text-brand-gold rounded-xl flex items-center justify-center font-bold text-xl"><i class="fa-solid fa-chart-line"></i></div>
          <h3 class="font-bold text-brand-navy">รายงาน Real-Time</h3>
          <p class="text-xs text-slate-600 font-['Sarabun'] leading-relaxed">รายงานสถิติวัดผล Performance อย่างโปร่งใส ตรวจสอบความคืบหน้ายอดขายได้ทันที</p>
        </div>
        <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
          <div class="w-12 h-12 bg-green-100 text-green-600 rounded-xl flex items-center justify-center font-bold text-xl"><i class="fa-solid fa-user-graduate"></i></div>
          <h3 class="font-bold text-brand-navy">ทีมงานผ่านการเทรนนิ่ง</h3>
          <p class="text-xs text-slate-600 font-['Sarabun'] leading-relaxed">พนักงานทุกคนผ่านการอบรมทักษะการเจรจาต่อรอง สคริปต์ปิดการขาย และมารยาทที่ดีเยี่ยม</p>
        </div>
        <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
          <div class="w-12 h-12 bg-purple-100 text-purple-600 rounded-xl flex items-center justify-center font-bold text-xl"><i class="fa-solid fa-bullhorn"></i></div>
          <h3 class="font-bold text-brand-navy">โทรเชิงรุกครบวงจร</h3>
          <p class="text-xs text-slate-600 font-['Sarabun'] leading-relaxed">ทั้งการเสนอขาย (Telesales), แจ้งเตือนโปรโมชั่น, สอบถามความพึงพอใจ และติดตามลูกค้าเก่า</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-brand-dark text-slate-400 py-10 text-center text-xs border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 space-y-3">
      <div>&copy; 2026 Tel2tellcallcenter.com | โทร: 089-040-4627 | LINE: manzx3</div>
      <div class="text-slate-500"><a href="index.html" class="hover:text-white">กลับหน้าแรก</a></div>
    </div>
  </footer>
</body>
</html>
"""

# 2. SALES ADMIN PAGE
sales_admin_html = """<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sales Admin ดูแลลูกค้า 24/7 | Tel2Tell Call Center</title>
  <link rel="icon" type="image/png" href="images/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Prompt:wght@300;400;500;600;700&family=Sarabun:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: { brand: { navy: '#1B2A38', dark: '#111923', card: '#223446', cyan: '#0EA5E9', accent: '#22D3EE', gold: '#F59E0B' } },
          fontFamily: { prompt: ['Prompt', 'sans-serif'], sarabun: ['Sarabun', 'sans-serif'] }
        }
      }
    }
  </script>
</head>
<body class="bg-slate-50 text-slate-800 font-['Prompt','Sarabun'] antialiased">
  <header class="sticky top-0 z-50 bg-[#1B2A38]/90 backdrop-blur border-b border-slate-700">
    <div class="max-w-7xl mx-auto px-4 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3">
        <img src="images/logo.png" alt="Tel2Tell" class="h-10 w-auto bg-white/90 p-1 rounded-lg">
        <span class="text-xl font-bold text-white font-['Prompt']">TEL2TELL</span>
      </a>
      <nav class="hidden md:flex items-center gap-6 text-sm text-slate-200">
        <a href="index.html" class="hover:text-brand-accent">หน้าแรก</a>
        <a href="outbound.html" class="hover:text-brand-accent">Outbound Callcenter</a>
        <a href="sales-admin.html" class="text-brand-accent font-bold">Sales Admin</a>
        <a href="vdo-production.html" class="hover:text-brand-accent">VDO Production</a>
        <a href="jobs.html" class="text-brand-gold font-semibold">รับสมัครงาน</a>
        <a href="index.html#contact" class="px-4 py-2 bg-brand-cyan text-white rounded-lg font-bold">ติดต่อเรา</a>
      </nav>
    </div>
  </header>

  <section class="bg-gradient-to-br from-brand-dark via-brand-navy to-slate-900 text-white py-20 border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7 space-y-6">
        <span class="px-3 py-1 bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 text-xs font-bold rounded-full">
          24/7 OMNICHANNEL SALES ADMIN
        </span>
        <h1 class="text-3xl sm:text-5xl font-extrabold leading-tight">
          Sales Admin มืออาชีพ ดูแลลูกค้า 24/7 ปิดการขายไว เพิ่มยอดขายปัง
        </h1>
        <p class="text-slate-300 text-base font-['Sarabun'] leading-relaxed">
          หยุดปัญหาตอบแชทช้า ลูกค้าหลุดไปหาคู่แข่ง หรือแอดมินลาออกบ่อย ด้วยบริการ Sales Admin Outsource จาก Tel2Tell ทีมงานพร้อมสลับกะตอบแชท คีย์ออเดอร์ ประสานงานจัดส่ง ตลอด 24 ชั่วโมง
        </p>
        <div class="flex gap-4 pt-2">
          <a href="index.html#contact" class="px-7 py-3.5 bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold rounded-xl shadow-lg transition">
            ประเมินค่าบริการฟรี
          </a>
          <a href="tel:0890404627" class="px-6 py-3.5 bg-slate-800 hover:bg-slate-700 text-white font-semibold rounded-xl border border-slate-700 flex items-center gap-2">
            <i class="fa-solid fa-phone"></i> 089-040-4627
          </a>
        </div>
      </div>
      <div class="lg:col-span-5">
        <img src="images/srv-social.jpg" alt="Sales Admin" class="rounded-2xl shadow-2xl border border-slate-700">
      </div>
    </div>
  </section>

  <!-- Problem & Solution -->
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 space-y-12">
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <h2 class="text-3xl font-extrabold text-brand-navy">ธุรกิจของคุณกำลังเจอปัญหาเหล่านี้หรือไม่?</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-6 rounded-2xl bg-red-50 border border-red-100 space-y-3">
          <i class="fa-solid fa-clock-rotate-left text-2xl text-red-500"></i>
          <h3 class="font-bold text-red-950">ตอบแชทช้า เสียลูกค้า</h3>
          <p class="text-xs text-red-800 font-['Sarabun'] leading-relaxed">ลูกค้ายุคใหม่ต้องการคำตอบภายใน 3 นาที หากตอบช้าเพียงนิดเดียว ลูกค้าจะเปลี่ยนไปสั่งซื้อจากร้านคู่แข่งทันที</p>
        </div>
        <div class="p-6 rounded-2xl bg-amber-50 border border-amber-100 space-y-3">
          <i class="fa-solid fa-moon text-2xl text-amber-500"></i>
          <h3 class="font-bold text-amber-950">เสียโอกาสตอนกลางคืน</h3>
          <p class="text-xs text-amber-800 font-['Sarabun'] leading-relaxed">ช่วงเวลา 20.00 - 02.00 น. คือช่วงช็อปปิ้งยอดนิยม แต่แอดมินประจำเลิกงานแล้ว ทำให้พลาดออเดอร์จำนวนมาก</p>
        </div>
        <div class="p-6 rounded-2xl bg-purple-50 border border-purple-100 space-y-3">
          <i class="fa-solid fa-user-xmark text-2xl text-purple-500"></i>
          <h3 class="font-bold text-purple-950">แอดมินลาออกบ่อย</h3>
          <p class="text-xs text-purple-800 font-['Sarabun'] leading-relaxed">ต้องเสียเวลาลงประกาศรับสมัคร สัมภาษณ์ และสอนงานใหม่อยู่ตลอดเวลา ทำให้ระบบการขายสะดุด</p>
        </div>
      </div>
    </div>
  </section>

  <footer class="bg-brand-dark text-slate-400 py-10 text-center text-xs border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 space-y-3">
      <div>&copy; 2026 Tel2tellcallcenter.com | โทร: 089-040-4627 | LINE: manzx3</div>
      <div class="text-slate-500"><a href="index.html" class="hover:text-white">กลับหน้าแรก</a></div>
    </div>
  </footer>
</body>
</html>
"""

# 3. VDO PRODUCTION PAGE
vdo_html = """<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VDO Production House ครบวงจร | Tel2Tell Call Center</title>
  <link rel="icon" type="image/png" href="images/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Prompt:wght@300;400;500;600;700&family=Sarabun:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: { brand: { navy: '#1B2A38', dark: '#111923', card: '#223446', cyan: '#0EA5E9', accent: '#22D3EE', gold: '#F59E0B' } },
          fontFamily: { prompt: ['Prompt', 'sans-serif'], sarabun: ['Sarabun', 'sans-serif'] }
        }
      }
    }
  </script>
</head>
<body class="bg-slate-50 text-slate-800 font-['Prompt','Sarabun'] antialiased">
  <header class="sticky top-0 z-50 bg-[#1B2A38]/90 backdrop-blur border-b border-slate-700">
    <div class="max-w-7xl mx-auto px-4 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3">
        <img src="images/logo.png" alt="Tel2Tell" class="h-10 w-auto bg-white/90 p-1 rounded-lg">
        <span class="text-xl font-bold text-white font-['Prompt']">TEL2TELL</span>
      </a>
      <nav class="hidden md:flex items-center gap-6 text-sm text-slate-200">
        <a href="index.html" class="hover:text-brand-accent">หน้าแรก</a>
        <a href="outbound.html" class="hover:text-brand-accent">Outbound Callcenter</a>
        <a href="sales-admin.html" class="hover:text-brand-accent">Sales Admin</a>
        <a href="vdo-production.html" class="text-brand-accent font-bold">VDO Production</a>
        <a href="jobs.html" class="text-brand-gold font-semibold">รับสมัครงาน</a>
        <a href="index.html#contact" class="px-4 py-2 bg-brand-cyan text-white rounded-lg font-bold">ติดต่อเรา</a>
      </nav>
    </div>
  </header>

  <section class="bg-gradient-to-br from-brand-dark via-brand-navy to-slate-900 text-white py-20 border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7 space-y-6">
        <span class="px-3 py-1 bg-purple-500/20 border border-purple-500/30 text-purple-300 text-xs font-bold rounded-full">
          PRODUCTION HOUSE & TV ADS
        </span>
        <h1 class="text-3xl sm:text-5xl font-extrabold leading-tight">
          รับจ้างถ่ายวีดีโอ VDO Production ครบวงจร หยุดนิ้วโป้ง เพิ่มยอดขาย
        </h1>
        <p class="text-slate-300 text-base font-['Sarabun'] leading-relaxed">
          สร้างสรรค์วิดีโอคุณภาพสูงที่ตอบโจทย์การทำการตลาด ตั้งแต่คิดคอนเซ็ปต์ ถ่ายทำ ตัดต่อ ไปจนถึงการยื่นตรวจเซ็นเซอร์ (Censored) สำหรับออกอากาศโทรทัศน์ และปรับสัดส่วนสำหรับโซเชียลมีเดีย TikTok, Reels, YouTube
        </p>
        <div class="flex gap-4 pt-2">
          <a href="index.html#contact" class="px-7 py-3.5 bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold rounded-xl shadow-lg transition">
            ขอใบเสนอราคาวิดีโอ
          </a>
          <a href="tel:0890404627" class="px-6 py-3.5 bg-slate-800 hover:bg-slate-700 text-white font-semibold rounded-xl border border-slate-700 flex items-center gap-2">
            <i class="fa-solid fa-phone"></i> 089-040-4627
          </a>
        </div>
      </div>
      <div class="lg:col-span-5">
        <img src="images/srv-spot-ads.jpg" alt="VDO Production" class="rounded-2xl shadow-2xl border border-slate-700">
      </div>
    </div>
  </section>

  <!-- Process -->
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 space-y-12">
      <div class="text-center max-w-2xl mx-auto space-y-3">
        <h2 class="text-3xl font-extrabold text-brand-navy">ขั้นตอนการทำงานแบบครบวงจร (End-to-End)</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
          <div class="text-3xl font-black text-brand-cyan">01</div>
          <h3 class="font-bold text-brand-navy">Pre-Production</h3>
          <p class="text-xs text-slate-600 font-['Sarabun'] leading-relaxed">วางแผนกลยุทธ์ คิดคอนเซ็ปต์ เขียนสคริปต์ ออกแบบ Storyboard คัดเลือกนักแสดง และจัดหาสถานที่ถ่ายทำ</p>
        </div>
        <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
          <div class="text-3xl font-black text-brand-gold">02</div>
          <h3 class="font-bold text-brand-navy">Production</h3>
          <p class="text-xs text-slate-600 font-['Sarabun'] leading-relaxed">ถ่ายทำด้วยกล้อง Cinema และทีมงานระดับมืออาชีพ ทั้งผู้กำกับ ตากล้อง ทีมไฟ และทีมบันทึกเสียงคุณภาพสูง</p>
        </div>
        <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
          <div class="text-3xl font-black text-purple-500">03</div>
          <h3 class="font-bold text-brand-navy">Post-Production & TV Censored</h3>
          <p class="text-xs text-slate-600 font-['Sarabun'] leading-relaxed">ตัดต่อลำดับภาพ ปรับแต่งโทนสี ทำ Motion Graphic ลงเสียงพากย์ และดำเนินการยื่นตรวจเซ็นเซอร์ออกอากาศทีวี</p>
        </div>
      </div>
    </div>
  </section>

  <footer class="bg-brand-dark text-slate-400 py-10 text-center text-xs border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 space-y-3">
      <div>&copy; 2026 Tel2tellcallcenter.com | โทร: 089-040-4627 | LINE: manzx3</div>
      <div class="text-slate-500"><a href="index.html" class="hover:text-white">กลับหน้าแรก</a></div>
    </div>
  </footer>
</body>
</html>
"""

# 4. JOBS & CAREERS PAGE
jobs_html = """<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ร่วมงานกับ เทล ทู เทล (เปิดรับสมัครงาน) | Tel2Tell Careers</title>
  <link rel="icon" type="image/png" href="images/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Prompt:wght@300;400;500;600;700&family=Sarabun:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: { brand: { navy: '#1B2A38', dark: '#111923', card: '#223446', cyan: '#0EA5E9', accent: '#22D3EE', gold: '#F59E0B' } },
          fontFamily: { prompt: ['Prompt', 'sans-serif'], sarabun: ['Sarabun', 'sans-serif'] }
        }
      }
    }
  </script>
</head>
<body class="bg-slate-50 text-slate-800 font-['Prompt','Sarabun'] antialiased">
  <header class="sticky top-0 z-50 bg-[#1B2A38]/90 backdrop-blur border-b border-slate-700">
    <div class="max-w-7xl mx-auto px-4 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3">
        <img src="images/logo.png" alt="Tel2Tell" class="h-10 w-auto bg-white/90 p-1 rounded-lg">
        <span class="text-xl font-bold text-white font-['Prompt']">TEL2TELL</span>
      </a>
      <nav class="hidden md:flex items-center gap-6 text-sm text-slate-200">
        <a href="index.html" class="hover:text-brand-accent">หน้าแรก</a>
        <a href="outbound.html" class="hover:text-brand-accent">Outbound Callcenter</a>
        <a href="sales-admin.html" class="hover:text-brand-accent">Sales Admin</a>
        <a href="vdo-production.html" class="hover:text-brand-accent">VDO Production</a>
        <a href="jobs.html" class="text-brand-gold font-bold">รับสมัครงาน</a>
        <a href="index.html#contact" class="px-4 py-2 bg-brand-cyan text-white rounded-lg font-bold">ติดต่อเรา</a>
      </nav>
    </div>
  </header>

  <section class="bg-gradient-to-br from-brand-dark via-brand-navy to-slate-900 text-white py-16 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto px-4 space-y-4">
      <span class="px-3 py-1 bg-amber-500/20 border border-amber-500/30 text-brand-gold text-xs font-bold rounded-full">
        WE ARE HIRING
      </span>
      <h1 class="text-3xl sm:text-5xl font-extrabold leading-tight">
        ร่วมงานกับ บริษัท เทล ทู เทล จำกัด
      </h1>
      <p class="text-slate-300 text-base font-['Sarabun'] leading-relaxed max-w-2xl mx-auto">
        เปิดรับสมัครพนักงานหลายอัตรา บรรยากาศเป็นกันเอง มีการเทรนนิ่งงานให้ รายได้ดี ค่าคอมมิชชั่นสูง และสวัสดิการครบครัน
      </p>
    </div>
  </section>

  <!-- Job Openings Grid -->
  <section class="py-16 max-w-7xl mx-auto px-4 space-y-12">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Card 1 -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm flex flex-col justify-between space-y-6">
        <div class="space-y-4">
          <span class="px-2.5 py-1 text-xs font-bold bg-amber-50 text-amber-700 rounded-full">รายได้ 15,000 - 40,000+ บาท</span>
          <h3 class="text-xl font-bold text-brand-navy">Telesales (พนักงานขายทางโทรศัพท์)</h3>
          <div class="text-xs text-slate-600 space-y-2 font-['Sarabun']">
            <p><strong>รายละเอียดงาน:</strong> เสนอขายสินค้าทางโทรศัพท์ มีรายชื่อลูกค้าให้พร้อม</p>
            <p><strong>คุณสมบัติ:</strong> ชาย/หญิง อายุ 18-40 ปี, วุฒิ ม.3 ขึ้นไป, พูดจาไพเราะ มั่นใจ</p>
            <p><strong>สถานที่:</strong> สุขุมวิท 62 (ใกล้ BTS บางจาก)</p>
          </div>
        </div>
        <a href="#applyForm" onclick="setApplyPos('Telesales')" class="w-full py-2.5 bg-brand-cyan hover:bg-sky-400 text-white font-bold text-sm rounded-xl text-center transition">
          กรอกใบสมัคร
        </a>
      </div>

      <!-- Card 2 -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm flex flex-col justify-between space-y-6">
        <div class="space-y-4">
          <span class="px-2.5 py-1 text-xs font-bold bg-emerald-50 text-emerald-700 rounded-full">เงินเดือนประจำ + เบี้ยขยัน</span>
          <h3 class="text-xl font-bold text-brand-navy">Admin (แอดมินเพจ / ตอบแชท)</h3>
          <div class="text-xs text-slate-600 space-y-2 font-['Sarabun']">
            <p><strong>รายละเอียดงาน:</strong> ตอบคำถาม ให้ข้อมูล แนะนำสินค้า และรับออเดอร์ทางแชท FB/LINE</p>
            <p><strong>คุณสมบัติ:</strong> ชาย/หญิง อายุ 18-35 ปี, พิมพ์เร็ว สื่อสารรู้เรื่อง มีไหวพริบ</p>
            <p><strong>สถานที่:</strong> สุขุมวิท 62 (ใกล้ BTS บางจาก)</p>
          </div>
        </div>
        <a href="#applyForm" onclick="setApplyPos('Admin')" class="w-full py-2.5 bg-brand-cyan hover:bg-sky-400 text-white font-bold text-sm rounded-xl text-center transition">
          กรอกใบสมัคร
        </a>
      </div>

      <!-- Card 3 -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm flex flex-col justify-between space-y-6">
        <div class="space-y-4">
          <span class="px-2.5 py-1 text-xs font-bold bg-purple-50 text-purple-700 rounded-full">รายได้ 11,000 + คอมมิชชั่น</span>
          <h3 class="text-xl font-bold text-brand-navy">Callcenter TV (รับสายรายการทีวี)</h3>
          <div class="text-xs text-slate-600 space-y-2 font-['Sarabun']">
            <p><strong>รายละเอียดงาน:</strong> รับสายและจำหน่ายสินค้าในรายการโทรทัศน์ (ทำเป็นกะ 09.00 - 23.00 น.)</p>
            <p><strong>คุณสมบัติ:</strong> ชาย/หญิง อายุ 18-40 ปี, วุฒิ ม.3 ขึ้นไป, รับแรงกดดันได้ดี</p>
            <p><strong>สถานที่:</strong> สุขุมวิท 62 (ใกล้ BTS บางจาก)</p>
          </div>
        </div>
        <a href="#applyForm" onclick="setApplyPos('Callcenter TV')" class="w-full py-2.5 bg-brand-cyan hover:bg-sky-400 text-white font-bold text-sm rounded-xl text-center transition">
          กรอกใบสมัคร
        </a>
      </div>

    </div>

    <!-- Application Form Container -->
    <div id="applyForm" class="max-w-2xl mx-auto bg-white rounded-2xl border border-slate-200 p-8 shadow-sm space-y-6">
      <h3 class="text-xl font-bold text-brand-navy pb-2 border-b border-slate-100">
        แบบฟอร์มสมัครงานออนไลน์ (สมัครและทราบผลทันที)
      </h3>
      <form onsubmit="handleJobPageSubmit(event)" class="space-y-4">
        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">ตำแหน่งที่ต้องการสมัคร <span class="text-red-500">*</span></label>
          <select id="posSelect" required class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan font-['Sarabun']">
            <option value="Telesales">Telesales (พนักงานขายทางโทรศัพท์)</option>
            <option value="Admin">Admin (แอดมินเพจ / ตอบแชท)</option>
            <option value="Callcenter TV">Callcenter TV (รับสายรายการทีวี)</option>
          </select>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">ชื่อ-นามสกุล <span class="text-red-500">*</span></label>
            <input type="text" required placeholder="นาย/นางสาว สมหวัง มุ่งมั่น" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">เบอร์โทรศัพท์ <span class="text-red-500">*</span></label>
            <input type="tel" required placeholder="08x-xxx-xxxx" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan">
          </div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">อายุ (ปี) <span class="text-red-500">*</span></label>
            <input type="number" min="18" max="50" required placeholder="25" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">วุฒิการศึกษาสูงสุด <span class="text-red-500">*</span></label>
            <select required class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan font-['Sarabun']">
              <option value="ม.3 / ม.6">ม.3 / ม.6</option>
              <option value="ปวช. / ปวส.">ปวช. / ปวส.</option>
              <option value="ปริญญาตรี">ปริญญาตรี</option>
            </select>
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">ประวัติการทำงาน / แนะนำตัวเองสั้นๆ</label>
          <textarea rows="3" placeholder="ระบุประสบการณ์ทำงานที่ผ่านมา..." class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan font-['Sarabun']"></textarea>
        </div>
        <button type="submit" class="w-full py-3.5 bg-brand-cyan hover:bg-sky-400 text-white font-bold rounded-xl shadow-lg transition">
          ส่งข้อมูลการสมัครงาน
        </button>
      </form>
    </div>
  </section>

  <footer class="bg-brand-dark text-slate-400 py-10 text-center text-xs border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 space-y-3">
      <div>&copy; 2026 Tel2tellcallcenter.com | โทร: 089-040-4627 | LINE: manzx3</div>
      <div class="text-slate-500"><a href="index.html" class="hover:text-white">กลับหน้าแรก</a></div>
    </div>
  </footer>

  <script>
    function setApplyPos(pos) {
      document.getElementById('posSelect').value = pos;
    }
    function handleJobPageSubmit(e) {
      e.preventDefault();
      alert('ส่งใบสมัครเรียบร้อยแล้ว! ฝ่ายบุคคล Tel2Tell จะโทรติดต่อกลับเพื่อนัดสัมภาษณ์งานครับ');
      e.target.reset();
    }
  </script>
</body>
</html>
"""

with open('outbound.html', 'w', encoding='utf-8') as f:
    f.write(outbound_html)
with open('sales-admin.html', 'w', encoding='utf-8') as f:
    f.write(sales_admin_html)
with open('vdo-production.html', 'w', encoding='utf-8') as f:
    f.write(vdo_html)
with open('jobs.html', 'w', encoding='utf-8') as f:
    f.write(jobs_html)

print("Generated outbound.html, sales-admin.html, vdo-production.html, jobs.html successfully!")
