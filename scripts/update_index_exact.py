import os

index_code = """<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Call Center เทล ทู เทล ให้บริการพร้อมทีมงานมืออาชีพ | Tel2tellcallcenter.com</title>
  <meta name="description" content="ผู้ให้บริการ Outsource Contact Center ครบวงจร ทั้งรับสายเข้า และโทรออก พร้อมทั้งแนะนำการตลาดออฟไลน์ และ ออนไลน์ ให้บริการอย่างมีคุณภาพมาตรฐานสากล เรามีนโยบายความปลอดภัยของข้อมูล และบริการครบวงจร">
  <meta name="keywords" content="Call center,โฆษณา,เทล ทู เทล,tel2tell">
  
  <!-- Favicon -->
  <link rel="icon" type="image/png" href="images/logo.png">

  <!-- Google Fonts: Lora, Open Sans, Prompt, Sarabun -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Open+Sans:wght@300;400;600;700&family=Prompt:wght@300;400;500;600;700&family=Sarabun:wght@300;400;500;600&display=swap" rel="stylesheet">
  
  <!-- Font Awesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            t2t: {
              navy: '#21333F',
              navyDark: '#1A2933',
              navyLight: '#2C4353',
              gold: '#CDB585',
              goldLight: '#E8D8B6',
              cyan: '#24BEE2',
              blue: '#1C3A79',
              line: '#00BC0C',
              grey: '#747474',
              bgLight: '#F8F9FA'
            }
          },
          fontFamily: {
            lora: ['Lora', 'serif'],
            prompt: ['Prompt', 'sans-serif'],
            sarabun: ['Sarabun', 'sans-serif'],
            open: ['Open Sans', 'sans-serif']
          }
        }
      }
    }
  </script>

  <style>
    body {
      font-family: 'Prompt', 'Open Sans', sans-serif;
      color: #333333;
    }
    h1, h2, h3.title-lora {
      font-family: 'Lora', 'Prompt', serif;
    }
    .bg-pattern {
      background-image: url('images/bg-pattern.jpg');
      background-repeat: no-repeat;
      background-position: center center;
      background-size: cover;
    }
    .bg-article-pattern {
      background-image: url('images/bg-article.jpg');
      background-repeat: no-repeat;
      background-position: center center;
      background-size: cover;
    }
    .card-zoom {
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card-zoom:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 24px -6px rgba(0, 0, 0, 0.2);
    }
    .divider-line {
      display: block;
      margin: 10px auto 18px auto;
      max-width: 140px;
      height: auto;
    }
  </style>
</head>
<body class="bg-white antialiased selection:bg-t2t-cyan selection:text-white">

  <!-- ============================================================== -->
  <!-- 1. HEADER & TOP NAVIGATION                                     -->
  <!-- ============================================================== -->
  <header class="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- Logo -->
        <a href="index.html" class="flex items-center gap-3">
          <img src="images/logo.png" alt="Tel2Tell Call Center" class="h-12 w-auto object-contain">
          <div class="flex flex-col">
            <span class="text-xl font-bold tracking-tight text-t2t-navy font-prompt">TEL2TELL</span>
            <span class="text-[10px] text-slate-500 font-semibold tracking-wider">CALL CENTER & MARKETING</span>
          </div>
        </a>

        <!-- Desktop Navigation Links (Original items) -->
        <nav class="hidden xl:flex items-center space-x-1 text-sm font-medium text-slate-700">
          <a href="index.html" class="px-3 py-2 text-t2t-cyan font-bold hover:text-t2t-navy transition">Home</a>
          <a href="https://arapapashop.com/" target="_blank" class="px-3 py-2 hover:text-t2t-cyan transition">Arapapa Shop</a>
          <a href="https://www.fgfulfill.com/" target="_blank" class="px-3 py-2 hover:text-t2t-cyan transition">FG Logistic</a>
          <a href="https://tel2solar.com/" target="_blank" class="px-3 py-2 hover:text-t2t-cyan transition">Tel2Solar</a>
          <a href="#contact" class="px-3 py-2 hover:text-t2t-cyan transition">Contact</a>
          <a href="#articles" class="px-3 py-2 hover:text-t2t-cyan transition">Forum</a>
          <a href="outbound.html" class="px-3 py-2 hover:text-t2t-cyan transition">Outbond Callcenter</a>
          <a href="vdo-production.html" class="px-3 py-2 hover:text-t2t-cyan transition">VDO Production</a>
          <a href="sales-admin.html" class="px-3 py-2 hover:text-t2t-cyan transition">Sales Admin</a>
          
          <!-- Dropdown "เพิ่มเติม" -->
          <div class="relative group">
            <button class="px-3 py-2 hover:text-t2t-cyan flex items-center gap-1 transition">
              <span>เพิ่มเติม</span>
              <i class="fa-solid fa-chevron-down text-[10px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </button>
            <div class="absolute right-0 mt-2 w-52 bg-white border border-slate-200 rounded-xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 p-2 z-50 text-xs">
              <a href="jobs.html" class="block px-3 py-2.5 rounded-lg hover:bg-slate-50 hover:text-t2t-cyan font-semibold text-amber-600">
                <i class="fa-solid fa-user-plus mr-2"></i> Work with us (สมัครงาน)
              </a>
              <a href="#performance" class="block px-3 py-2.5 rounded-lg hover:bg-slate-50 hover:text-t2t-cyan">
                <i class="fa-solid fa-award mr-2 text-t2t-gold"></i> รางวัล & Performance
              </a>
              <a href="#whyus" class="block px-3 py-2.5 rounded-lg hover:bg-slate-50 hover:text-t2t-cyan">
                <i class="fa-solid fa-shield-halved mr-2 text-cyan-600"></i> ทำไมต้องเลือกเรา (Why Us)
              </a>
              <a href="#clients" class="block px-3 py-2.5 rounded-lg hover:bg-slate-50 hover:text-t2t-cyan">
                <i class="fa-solid fa-handshake mr-2 text-blue-600"></i> ลูกค้าของเรา (Our Clients)
              </a>
            </div>
          </div>
        </nav>

        <!-- Quick Call & Mobile Toggle -->
        <div class="flex items-center gap-3">
          <a href="tel:0890404627" class="hidden sm:inline-flex items-center gap-2 bg-t2t-navy hover:bg-t2t-navyLight text-white text-xs font-semibold px-4 py-2.5 rounded-lg shadow-sm transition">
            <i class="fa-solid fa-phone text-t2t-gold"></i>
            <span>089-040-4627</span>
          </a>

          <!-- Mobile Toggle Button -->
          <button id="mobileMenuToggle" class="xl:hidden p-2 rounded-lg text-slate-700 hover:text-t2t-navy focus:outline-none">
            <i class="fa-solid fa-bars text-2xl"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- Mobile Drawer Menu -->
    <div id="mobileDrawer" class="hidden xl:hidden bg-white border-b border-slate-200 px-4 pt-2 pb-6 space-y-2 text-sm font-medium text-slate-700">
      <a href="index.html" class="block px-3 py-2 rounded-lg bg-slate-100 text-t2t-cyan font-bold">Home (หน้าแรก)</a>
      <a href="outbound.html" class="block px-3 py-2 rounded-lg hover:bg-slate-50">Outbond Callcenter</a>
      <a href="vdo-production.html" class="block px-3 py-2 rounded-lg hover:bg-slate-50">VDO Production</a>
      <a href="sales-admin.html" class="block px-3 py-2 rounded-lg hover:bg-slate-50">Sales Admin</a>
      <a href="jobs.html" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-amber-600 font-bold">Work with us (รับสมัครงาน)</a>
      <a href="https://arapapashop.com/" target="_blank" class="block px-3 py-2 rounded-lg hover:bg-slate-50">Arapapa Shop</a>
      <a href="https://www.fgfulfill.com/" target="_blank" class="block px-3 py-2 rounded-lg hover:bg-slate-50">FG Logistic</a>
      <a href="https://tel2solar.com/" target="_blank" class="block px-3 py-2 rounded-lg hover:bg-slate-50">Tel2Solar</a>
      <a href="#contact" class="block px-3 py-2 rounded-lg hover:bg-slate-50">Contact (ติดต่อเรา)</a>
      <div class="pt-2">
        <a href="tel:0890404627" class="w-full bg-t2t-navy text-white py-2.5 rounded-lg font-bold text-center block text-xs">
          <i class="fa-solid fa-phone mr-1.5 text-t2t-gold"></i> โทร: 089-040-4627
        </a>
      </div>
    </div>
  </header>

  <!-- ============================================================== -->
  <!-- 2. HERO BANNER (Full width matching original Section 2)        -->
  <!-- ============================================================== -->
  <section class="w-full bg-slate-100 overflow-hidden border-b border-slate-200">
    <div class="w-full">
      <img src="images/hero-banner.jpg" alt="Tel2Tell Call Center Banner" class="w-full h-auto object-cover max-h-[580px] mx-auto">
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 3. OUR SERVICE (Section 3 - Navy Background)                  -->
  <!-- ============================================================== -->
  <section id="services" class="py-12 bg-t2t-navy text-white text-center">
    <div class="max-w-4xl mx-auto px-4 space-y-2">
      <h2 class="text-3xl font-lora font-normal text-white tracking-wide">
        Our Service
      </h2>
      <img src="images/line-divider.png" alt="divider" class="divider-line">
      <h3 class="text-sm sm:text-base font-normal text-slate-200 leading-relaxed font-sarabun max-w-3xl mx-auto">
        เรามีบริการครอบคลุมหลากหลายพร้อมทั้งท้าทายทุกความต้องการของลูกค้าในทุกอุตสาหกรรม<br class="hidden sm:inline">
        เรามุ่งมั่นและใส่ใจเต็มที่ในการทำงานเพื่อให้ได้ผลงานที่มีคุณภาพ
      </h3>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 4. 4 SERVICE CARDS (Section 4 - Navy Background)               -->
  <!-- ============================================================== -->
  <section class="pb-14 bg-t2t-navy text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Service 1: Inbound Callcenter -->
        <div class="flex flex-col items-center text-center space-y-3 group cursor-pointer" onclick="location.href='#contact'">
          <div class="w-full rounded-lg overflow-hidden bg-slate-800 border border-slate-700/60 shadow-md card-zoom">
            <img src="images/srv-inbound.jpg" alt="Inbound Callcenter" class="w-full h-44 object-cover">
          </div>
          <h2 class="text-base font-semibold text-white group-hover:text-t2t-cyan transition font-prompt">
            Inbound Callcenter
          </h2>
        </div>

        <!-- Service 2: Outbound Callcenter -->
        <div class="flex flex-col items-center text-center space-y-3 group cursor-pointer" onclick="location.href='outbound.html'">
          <div class="w-full rounded-lg overflow-hidden bg-slate-800 border border-slate-700/60 shadow-md card-zoom">
            <img src="images/srv-outbound.jpg" alt="Outbound Callcenter" class="w-full h-44 object-cover">
          </div>
          <h2 class="text-base font-semibold text-white group-hover:text-t2t-cyan transition font-prompt">
            Outbound Callcenter
          </h2>
        </div>

        <!-- Service 3: Social Media Support -->
        <div class="flex flex-col items-center text-center space-y-3 group cursor-pointer" onclick="location.href='sales-admin.html'">
          <div class="w-full rounded-lg overflow-hidden bg-slate-800 border border-slate-700/60 shadow-md card-zoom">
            <img src="images/srv-social.jpg" alt="Social Media Support" class="w-full h-44 object-cover">
          </div>
          <h2 class="text-base font-semibold text-white group-hover:text-t2t-cyan transition font-prompt">
            Social Media Support
          </h2>
        </div>

        <!-- Service 4: Onsite Service -->
        <div class="flex flex-col items-center text-center space-y-3 group cursor-pointer" onclick="location.href='#contact'">
          <div class="w-full rounded-lg overflow-hidden bg-slate-800 border border-slate-700/60 shadow-md card-zoom">
            <img src="images/srv-onsite.jpg" alt="Onsite Service" class="w-full h-44 object-cover">
          </div>
          <h2 class="text-base font-semibold text-white group-hover:text-t2t-cyan transition font-prompt">
            Onsite Service
          </h2>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 5. 3 MEDIA & SYSTEM CARDS (Section 5 - Navy Background)        -->
  <!-- ============================================================== -->
  <section class="pb-16 bg-t2t-navy text-white border-t border-slate-700/40 pt-4">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Media Card 1 -->
        <div class="flex flex-col items-center text-center space-y-3 group cursor-pointer" onclick="location.href='vdo-production.html'">
          <div class="w-full rounded-lg overflow-hidden bg-slate-800 border border-slate-700/60 shadow-md card-zoom">
            <img src="images/srv-spot-ads.jpg" alt="รับผลิตสื่อโฆษณา Spot" class="w-full h-48 object-cover">
          </div>
          <div class="space-y-1">
            <h2 class="text-base font-bold text-white group-hover:text-t2t-cyan transition">
              รับผลิตสื่อโฆษณา Spot ทุกประเภทสินค้า
            </h2>
            <h2 class="text-sm font-semibold text-t2t-gold">
              พร้อมยื่น Censored
            </h2>
          </div>
        </div>

        <!-- Media Card 2 -->
        <div class="flex flex-col items-center text-center space-y-3 group cursor-pointer" onclick="location.href='#contact'">
          <div class="w-full rounded-lg overflow-hidden bg-slate-800 border border-slate-700/60 shadow-md card-zoom">
            <img src="images/srv-tv-air.jpg" alt="ลงสื่อโฆษณาทางทีวี" class="w-full h-48 object-cover">
          </div>
          <div class="space-y-1">
            <h2 class="text-base font-bold text-white group-hover:text-t2t-cyan transition">
              เพิ่มยอดขายช่องทางออฟไลน์
            </h2>
            <h2 class="text-sm font-semibold text-t2t-gold">
              ลงสื่อโฆษณาทางทีวี
            </h2>
          </div>
        </div>

        <!-- Media Card 3 -->
        <div class="flex flex-col items-center text-center space-y-3 group cursor-pointer" onclick="location.href='#contact'">
          <div class="w-full rounded-lg overflow-hidden bg-slate-800 border border-slate-700/60 shadow-md card-zoom">
            <img src="images/srv-cloud-pbx.jpg" alt="Call center ระบบCall center IP PBX" class="w-full h-48 object-cover">
          </div>
          <div class="space-y-1">
            <h1 class="text-base font-bold text-white group-hover:text-t2t-cyan transition">
              Call center
            </h1>
            <h2 class="text-xs font-semibold text-t2t-gold">
              ระบบCall center IP PBX ระบบCall center on cloud
            </h2>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 6. 12 YEARS EXPERIENCE (Section 6 - Navy Background)           -->
  <!-- ============================================================== -->
  <section class="py-14 bg-t2t-navy text-white text-center border-t border-slate-700/50">
    <div class="max-w-4xl mx-auto px-4 space-y-3">
      <h2 class="text-3xl font-lora font-normal text-white tracking-wide">
        12 Years Experience
      </h2>
      <img src="images/line-divider.png" alt="divider" class="divider-line">
      
      <div class="space-y-1.5 text-sm sm:text-base font-normal text-slate-200 font-sarabun max-w-3xl mx-auto leading-relaxed">
        <h3 class="font-normal">เราเป็นผู้ให้บริการด้าน Outsource Contact Center และการตลาดครบวงจร</h3>
        <h3 class="font-normal">รวมถึงบริการด้านการขาย การสร้างความสัมพันธ์กับลูกค้า ช่องทางออนไลน์ และ ออฟไลน์</h3>
        <h3 class="font-normal">งานคอลเซ็นเตอร์ ระบบคอลเซ็นเตอร์ งานโปรดักชั่น สื่อโฆษณาทางโทรทัศน์ และคลังสินค้า</h3>
      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 7. 6 CAPABILITIES (Section 7 - Light Pattern Background)       -->
  <!-- ============================================================== -->
  <section class="py-16 bg-pattern bg-slate-50 border-y border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Cap 1 -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden card-zoom">
          <img src="images/cap-outsource.jpg" alt="Outsource Service Center" class="w-full h-48 object-cover">
          <div class="p-4 text-center font-bold text-slate-800 text-sm font-prompt">
            Outsource Service Center
          </div>
        </div>

        <!-- Cap 2 -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden card-zoom">
          <img src="images/cap-pbx.jpg" alt="ระบบCall center" class="w-full h-48 object-cover">
          <div class="p-4 text-center font-bold text-slate-800 text-sm font-prompt">
            ระบบCall center
          </div>
        </div>

        <!-- Cap 3 -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden card-zoom">
          <img src="images/cap-tv.jpg" alt="สื่อโฆษณาทางโทรทัศน์" class="w-full h-48 object-cover">
          <div class="p-4 text-center font-bold text-slate-800 text-sm font-prompt">
            สื่อโฆษณาทางโทรทัศน์
          </div>
        </div>

        <!-- Cap 4 -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden card-zoom">
          <img src="images/cap-import-export.jpg" alt="Import&Export" class="w-full h-48 object-cover">
          <div class="p-4 text-center font-bold text-slate-800 text-sm font-prompt">
            Import&Export
          </div>
        </div>

        <!-- Cap 5 -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden card-zoom">
          <img src="images/cap-data-analysis.jpg" alt="Data Analysis" class="w-full h-48 object-cover">
          <div class="p-4 text-center font-bold text-slate-800 text-sm font-prompt">
            Data Analysis
          </div>
        </div>

        <!-- Cap 6 -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden card-zoom">
          <img src="images/cap-fulfillment.jpg" alt="Fulfillment" class="w-full h-48 object-cover">
          <div class="p-4 text-center font-bold text-slate-800 text-sm font-prompt">
            Fulfillment
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 8. OUR CLIENTS (Section 8 - Navy Background)                   -->
  <!-- ============================================================== -->
  <section id="clients" class="py-14 bg-t2t-navy text-white text-center">
    <div class="max-w-5xl mx-auto px-4 space-y-3">
      <h2 class="text-3xl font-lora font-normal text-white tracking-wide">
        Our Clients
      </h2>
      <img src="images/line-divider.png" alt="divider" class="divider-line">
      <h3 class="text-sm font-normal text-slate-300 font-sarabun">
        ขอขอบคุณลูกค้าที่วางใจและใช้บริการ บริษัท เทล ทู เทล จำกัด
      </h3>
      <div class="pt-6">
        <img src="images/client-logos.jpg" alt="Client Logos" class="w-full max-w-4xl mx-auto rounded-lg shadow-lg">
      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 9. PERFORMANCE (Section 9 - Light Background)                  -->
  <!-- ============================================================== -->
  <section id="performance" class="py-16 bg-white text-slate-800 border-y border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-4">
      <h2 class="text-3xl font-lora font-normal text-t2t-navy tracking-wide">
        Performance
      </h2>
      <img src="images/line-divider.png" alt="divider" class="divider-line">

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pt-6">
        
        <!-- Item 1: 1668 -->
        <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 shadow-sm flex flex-col items-center space-y-3">
          <div class="w-full h-44 rounded-lg overflow-hidden bg-slate-200">
            <img src="images/award-1668.jpg" alt="สายด่วน 1668" class="w-full h-full object-cover">
          </div>
          <h4 class="text-xs font-semibold text-slate-700 leading-snug font-sarabun text-center">
            สนับสนุนและร่วมมือในการร่วมเป็น Call Centerให้กับศูนย์ประสานงานการจัดหาเตียงสำหรับประชาชน สายด่วนกรมการแพทย์ 1668
          </h4>
        </div>

        <!-- Item 2: TCCTA Gold -->
        <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 shadow-sm flex flex-col items-center space-y-3">
          <div class="w-full h-44 rounded-lg overflow-hidden bg-slate-200">
            <img src="images/award-tccta-gold.jpg" alt="TCCTA Gold Award" class="w-full h-full object-cover">
          </div>
          <h4 class="text-xs font-semibold text-slate-700 leading-snug font-sarabun text-center">
            TCCTA GOLD AWARD The Best Corperate Social Responsibility
          </h4>
        </div>

        <!-- Item 3: TCCTA Award -->
        <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 shadow-sm flex flex-col items-center space-y-3">
          <div class="w-full h-44 rounded-lg overflow-hidden bg-slate-200">
            <img src="images/award-tccta-covid.jpg" alt="TCCTA Covid Award" class="w-full h-full object-cover">
          </div>
          <h4 class="text-xs font-semibold text-slate-700 leading-snug font-sarabun text-center">
            TCCTA AWARD ผู้ให้การสนับสนุนในโครงการรับเรื่องและช่วยเหลือผู่ป่วยโควิด 19
          </h4>
        </div>

        <!-- Item 4: Atmosphere -->
        <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 shadow-sm flex flex-col items-center space-y-3">
          <div class="w-full h-44 rounded-lg overflow-hidden bg-slate-200">
            <img src="images/atmosphere.gif" alt="ภาพบรรยากาศการทำงาน" class="w-full h-full object-cover">
          </div>
          <h4 class="text-xs font-semibold text-slate-700 leading-snug font-sarabun text-center">
            ภาพบรรยากาศการทำงาน
          </h4>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 10. AFFILIATE BANNER (Section 10 - Navy Background)             -->
  <!-- ============================================================== -->
  <section class="py-10 bg-t2t-navy text-center">
    <div class="max-w-4xl mx-auto px-4">
      <a href="https://www.dhipaya-training.com/" target="_blank" class="inline-block transition transform hover:scale-[1.01]">
        <img src="images/dhipaya-training.png" alt="ศูนย์ฝึกอบรม Dhipaya Training" class="w-full max-w-3xl mx-auto rounded-lg shadow-lg">
      </a>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 11. WHY US (Section 11 - Navy Background)                      -->
  <!-- ============================================================== -->
  <section id="whyus" class="py-16 bg-t2t-navy text-white text-center border-t border-slate-700/60">
    <div class="max-w-4xl mx-auto px-4 space-y-4">
      <h2 class="text-3xl font-lora font-normal text-white tracking-wide">
        Why Us
      </h2>
      <img src="images/line-divider.png" alt="divider" class="divider-line">
      
      <div class="max-w-2xl mx-auto text-left space-y-3 pt-4 font-sarabun text-sm sm:text-base text-slate-200">
        <div class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-800/40 transition">
          <i class="fa-solid fa-check-circle text-t2t-gold mt-1"></i>
          <span>เทล ทู เทล ผู้ให้บริการอย่างมีคุณภาพมาตรฐานสากล</span>
        </div>
        <div class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-800/40 transition">
          <i class="fa-solid fa-check-circle text-t2t-gold mt-1"></i>
          <span>นโยบายความปลอดภัยของข้อมูล</span>
        </div>
        <div class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-800/40 transition">
          <i class="fa-solid fa-check-circle text-t2t-gold mt-1"></i>
          <span>กฏเกณฑ์ภายในเรื่องความปลอดภัยของข้อมูล</span>
        </div>
        <div class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-800/40 transition">
          <i class="fa-solid fa-check-circle text-t2t-gold mt-1"></i>
          <span>ความเชี่ยวชาญในหลากหลายอุตสาหกรรม</span>
        </div>
        <div class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-800/40 transition">
          <i class="fa-solid fa-check-circle text-t2t-gold mt-1"></i>
          <span>เรามีบริการครบวงจร ทั้งงานด้านโลจิสติก และ บริการคลังสินค้า</span>
        </div>
        <div class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-800/40 transition">
          <i class="fa-solid fa-check-circle text-t2t-gold mt-1"></i>
          <span>ระบบจัดการออเดอร์ ที่เรียบง่าย และ สะดวกสบาย</span>
        </div>
        <div class="flex items-start gap-3 p-2 rounded-lg hover:bg-slate-800/40 transition">
          <i class="fa-solid fa-check-circle text-t2t-gold mt-1"></i>
          <span>รับปรึกษางานด้านการตลาดออฟไลน์ และ ออนไลน์ฟรี</span>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 12. ARTICLES (Section 12 - Background Article Pattern)         -->
  <!-- ============================================================== -->
  <section id="articles" class="py-16 bg-article-pattern bg-slate-100 border-y border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center space-y-3 mb-10">
        <h2 class="text-3xl font-prompt font-bold text-t2t-navy">
          บทความ
        </h2>
        <div class="w-12 h-1 bg-t2t-cyan mx-auto rounded-full"></div>
      </div>

      <!-- 8 Featured Articles Grid (Exact from original site) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Art 1 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_1.png" alt="รับจ้างถ่ายวีดีโอ VDO Production ครบวงจร" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30934')">
                รับจ้างถ่ายวีดีโอ VDO Production ครบวงจร | Tel2tell
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                Tel2tell รับจ้างถ่ายวีดีโอ VDO Production ครบวงจร ตั้งแต่คิดคอนเซ็ปต์ ถ่ายทำ ตัดต่อ พร้อมทีมงานมืออาชีพและอุปกรณ์ทันสมัย รองรับทุกแพลตฟอร์มออนไลน์ เพื่อสร้างวิดีโอคุณภาพสูงที่ช่วยเพิ่มยอดขายและสร้างแบรนด์ให้โดดเด่น
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30934')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

        <!-- Art 2 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_2.png" alt="ถ่ายวิดีโอให้ เวิร์ก ต้องเลือกให้ถูก" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30933')">
                ถ่ายวิดีโอให้ เวิร์ก ต้องเลือกให้ถูก! เปิดเบื้องหลังการสร้างสรรค์ด้วย production house มืออาชีพ
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                ค้นพบเหตุผลที่ธุรกิจยุคใหม่เลือกใช้ Production House มืออาชีพเพื่อสร้างสรรค์วิดีโอที่ทรงพลัง ตั้งแต่การคิดไอเดียไปจนถึงการตัดต่อ เพื่อยกระดับแบรนด์และสร้างผลลัพธ์ที่วัดผลได้จริง
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30933')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

        <!-- Art 3 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_3.png" alt="เปลี่ยนทุกสายโทรเป็นโอกาสทอง" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30932')">
                เปลี่ยนทุกสายโทรเป็นโอกาสทอง! ทำไมธุรกิจยุคใหม่ต้องใช้บริการลูกค้าแบบ Outbound Callcenter
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                ค้นพบว่าทำไม Outbound Callcenter ถึงเป็นเครื่องมือสำคัญสำหรับธุรกิจยุคใหม่ในการเข้าหาลูกค้าเชิงรุก สร้างความสัมพันธ์ที่ยั่งยืน และเพิ่มโอกาสทางธุรกิจ พลิกโฉมบริการลูกค้าของคุณให้เหนือกว่าคู่แข่ง
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30932')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

        <!-- Art 4 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_4.png" alt="หยิบโทรศัพท์ แล้วให้ธุรกิจวิ่งเข้าหาลูกค้า" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30931')">
                หยิบโทรศัพท์ แล้วให้ธุรกิจวิ่งเข้าหาลูกค้า!
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                เปลี่ยนทุกสายโทรศัพท์ให้เป็นยอดขายด้วย Outbound Callcenter และทีม Telesales มืออาชีพ! เข้าถึงลูกค้าเชิงรุก ประหยัดต้นทุน และวัดผลได้จริง เหมาะสำหรับทุกธุรกิจที่ต้องการเพิ่มยอดขายอย่างรวดเร็ว
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30931')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

        <!-- Art 5 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_5.png" alt="Outbound Callcenter ยุคใหม่" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30930')">
                Outbound Callcenter ยุคใหม่: พลิกโฉมธุรกิจด้วยการสื่อสารลูกค้าสัมพันธ์อย่างมืออาชีพ
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                เพิ่มยอดขายและรักษาฐานลูกค้าด้วยบริการ Outbound Callcenter ยุคใหม่ ที่ช่วยสร้างลูกค้าสัมพันธ์แข็งแกร่ง พร้อมเทคโนโลยีและทีมงานมืออาชีพ
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30930')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

        <!-- Art 6 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_6.png" alt="เปลี่ยนทุกพื้นที่ให้มีชีวิต" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30929')">
                เปลี่ยนทุกพื้นที่ให้มีชีวิต! เบื้องหลังงานอีเว้นท์สุดว้าวที่คุณก็จัดได้ ด้วยบริษัทจัดงานอีเว้นท์มืออาชีพ
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                บริษัทจัดงานอีเว้นท์มืออาชีพ พร้อมเนรมิตงาน Event Production ของคุณให้เหนือความคาดหมาย! สร้างประสบการณ์น่าจดจำ เพิ่มยอดขาย ด้วยกลยุทธ์การออกแบบและวางแผนอีเว้นท์แบบครบวงจร
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30929')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

        <!-- Art 7 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_7.png" alt="ถอดรหัส Event Production" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30928')">
                ถอดรหัส Event Production: เนรมิตอีเวนต์ในฝันให้กลายเป็นจริง
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                ยกระดับงานของคุณให้เป็น "ประสบการณ์" สุดประทับใจ! เจาะลึก Event Production ศาสตร์และศิลป์ที่ออแกไนซ์จัดงานมืออาชีพใช้เปลี่ยนอีเวนต์ธรรมดาให้เป็นความจริงสุดว้าว ที่ทุกคนต้องจดจำ
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30928')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

        <!-- Art 8 -->
        <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm flex flex-col justify-between card-zoom">
          <div>
            <div class="h-44 overflow-hidden bg-slate-100">
              <img src="images/articles/art_8.png" alt="ปลดล็อกพลัง VDO Production" class="w-full h-full object-cover">
            </div>
            <div class="p-4 space-y-2">
              <h3 class="font-bold text-sm text-t2t-navy line-clamp-2 hover:text-t2t-cyan cursor-pointer" onclick="openArticleModal('30927')">
                ปลดล็อกพลัง VDO Production: หยุดนิ้วโป้ง สร้างแบรนด์ให้โตด้วยวิดีโอ
              </h3>
              <p class="text-xs text-slate-600 font-sarabun line-clamp-3 leading-relaxed">
                บริการ VDO Production ที่ไม่ใช่แค่ภาพสวย แต่คือเครื่องมือสร้างการเติบโตทางธุรกิจ เราเปลี่ยนกลยุทธ์ให้เป็นวิดีโอที่ทรงพลัง เล่าเรื่องเก่ง หยุดนิ้วโป้งผู้ชม และเปลี่ยนให้พวกเขากลายเป็นลูกค้าของคุณ
              </p>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="openArticleModal('30927')" class="text-xs font-semibold text-t2t-cyan hover:text-blue-700 flex items-center gap-1">
              ดูเพิ่มเติม &rarr;
            </button>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 13. WORK WITH US (Section 13 - Navy Background)                -->
  <!-- ============================================================== -->
  <section class="py-16 bg-t2t-navy text-white text-center">
    <div class="max-w-5xl mx-auto px-4 space-y-4">
      <h2 class="text-3xl font-lora font-normal text-white tracking-wide">
        Work With Us
      </h2>
      <img src="images/line-divider.png" alt="divider" class="divider-line">
      
      <!-- Video Container -->
      <div class="max-w-3xl mx-auto rounded-xl overflow-hidden shadow-2xl bg-black aspect-video mt-6 border border-slate-700">
        <iframe class="w-full h-full" src="https://www.youtube.com/embed/tcVvzUBzVmQ" title="Work With Us Tel2tell" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>

      <div class="pt-6">
        <a href="jobs.html" class="inline-flex items-center gap-2 px-6 py-3 bg-t2t-gold hover:bg-amber-400 text-slate-900 font-bold text-sm rounded-lg transition shadow-md">
          <i class="fa-solid fa-briefcase"></i>
          <span>ดูตำแหน่งงานว่าง & กรอกใบสมัครออนไลน์</span>
        </a>
      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 14. CONTACT US TITLE (Section 14 - Navy Background)             -->
  <!-- ============================================================== -->
  <section class="py-12 bg-t2t-navy text-white text-center border-t border-slate-700/60">
    <div class="max-w-4xl mx-auto px-4 space-y-2">
      <h2 class="text-3xl font-lora font-normal text-white tracking-wide">
        Contact Us
      </h2>
      <img src="images/line-divider.png" alt="divider" class="divider-line">
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 15. CONTACT US FORM (Section 15 - Light Pattern Background)    -->
  <!-- ============================================================== -->
  <section id="contact" class="py-16 bg-pattern bg-slate-50 border-b border-slate-200">
    <div class="max-w-2xl mx-auto px-4">
      <form id="contactForm" class="bg-white/95 rounded-2xl border border-slate-200 p-8 shadow-sm space-y-5" onsubmit="handleContactSubmit(event)">
        
        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">ชื่อ <span class="text-red-500">*</span></label>
          <input type="text" id="inputName" required placeholder="ชื่อ" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm focus:outline-none focus:ring-1 focus:ring-t2t-cyan">
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">เบอร์โทรศัพท์ <span class="text-red-500">*</span></label>
          <input type="tel" id="inputPhone" required placeholder="เบอร์โทรศัพท์" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm focus:outline-none focus:ring-1 focus:ring-t2t-cyan">
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">E-mail</label>
          <input type="email" id="inputEmail" placeholder="E-mail" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm focus:outline-none focus:ring-1 focus:ring-t2t-cyan">
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">ข้อความ <span class="text-red-500">*</span></label>
          <textarea id="inputMessage" required rows="4" placeholder="ข้อความ" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm focus:outline-none focus:ring-1 focus:ring-t2t-cyan font-sarabun"></textarea>
        </div>

        <!-- Captcha -->
        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
          <span id="captchaText" class="font-bold text-sm text-t2t-navy">6 + 2 = ?</span>
          <input type="number" id="captchaAns" required placeholder="ตอบ" class="w-24 bg-white border border-slate-300 rounded px-2.5 py-1 text-sm text-center">
          <button type="button" onclick="genCaptcha()" class="text-xs text-slate-500 hover:text-t2t-cyan">
            <i class="fa-solid fa-rotate-right"></i> เปลี่ยนเลข
          </button>
        </div>

        <button type="submit" class="w-full py-3 bg-t2t-navy hover:bg-t2t-navyLight text-white font-bold text-sm rounded-lg transition shadow">
          ส่งข้อความ
        </button>
      </form>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- 16. FOOTER (Matching Section-Footer - Navy Background)         -->
  <!-- ============================================================== -->
  <footer class="bg-t2t-navy text-slate-300 pt-14 pb-8 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-10 pb-12 border-b border-slate-700">
        
        <!-- Col 1: Contact Us & Subscribe -->
        <div class="space-y-3">
          <h2 class="text-lg font-lora font-bold text-white tracking-wider">
            CONTACT US
          </h2>
          <h4 class="text-base font-bold text-white tracking-wide">
            0890404627
          </h4>
          <h4 class="text-xs text-slate-300">
            EMAIL nattapon@tel2tell.com
          </h4>
          
          <div class="pt-3 space-y-2">
            <div class="text-xs text-slate-400">ลงทะเบียนเพื่อรับข่าวสารจากเรา</div>
            <form onsubmit="handleSub(event)" class="flex gap-2">
              <input type="email" required placeholder="Email" class="bg-slate-800 border border-slate-600 rounded px-3 py-1.5 text-xs text-white focus:outline-none flex-1">
              <button type="submit" class="bg-t2t-cyan hover:bg-sky-400 text-slate-900 font-bold px-3 py-1.5 rounded text-xs transition">
                Subscribe
              </button>
            </form>
          </div>
        </div>

        <!-- Col 2: Social Links -->
        <div class="space-y-4 text-center md:text-left">
          <h4 class="text-sm font-bold text-white">ช่องทางโซเชียลมีเดีย</h4>
          <div class="flex items-center justify-center md:justify-start gap-4 text-2xl">
            <a href="https://www.facebook.com/Tel2tellcallcenter" target="_blank" class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center hover:scale-110 transition" title="Facebook">
              <i class="fa-brands fa-facebook-f text-base"></i>
            </a>
            <a href="https://www.youtube.com/channel/UCk_17vNw0lJKEmJXoP2gyzQ" target="_blank" class="w-10 h-10 rounded-full bg-red-600 text-white flex items-center justify-center hover:scale-110 transition" title="YouTube">
              <i class="fa-brands fa-youtube text-base"></i>
            </a>
            <a href="http://line.me/ti/p/~manzx3" target="_blank" class="w-10 h-10 rounded-full bg-green-500 text-white flex items-center justify-center hover:scale-110 transition" title="LINE ID: manzx3">
              <i class="fa-brands fa-line text-xl"></i>
            </a>
          </div>
        </div>

        <!-- Col 3: Company Network Links -->
        <div class="space-y-2 text-xs">
          <h4 class="text-sm font-bold text-white mb-2">กลุ่มบริษัทในเครือ</h4>
          <div><a href="https://www.facebook.com/Tel2tellcallcenter" target="_blank" class="hover:text-t2t-cyan">SEBIZ</a></div>
          <div><a href="https://www.facebook.com/Tel2tellcallcenter" target="_blank" class="hover:text-t2t-cyan">Tel2tell</a></div>
          <div><a href="https://www.facebook.com/Friendlygl" target="_blank" class="hover:text-t2t-cyan">FG Logistics</a></div>
          <div><a href="jobs.html" class="hover:text-t2t-gold font-semibold">Work with us</a></div>
        </div>

      </div>

      <!-- Bottom Bar & Visitor Stats -->
      <div class="pt-6 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <div>
          <h3>@ Copyright 2017 All Rights Reserved. Tel2tellcallcenter.com</h3>
        </div>

        <!-- Visitor Stats Counter -->
        <div class="flex items-center gap-4 text-[11px]">
          <span>ผู้เข้าชมทั้งหมด: <strong class="text-white">323,385</strong></span>
          <span>ผู้เข้าชมวันนี้: <strong class="text-green-400">215</strong></span>
          <span>ผู้เข้าชมขณะนี้: <strong class="text-t2t-cyan font-bold">42</strong></span>
        </div>
      </div>

    </div>
  </footer>

  <!-- Floating Contact Buttons -->
  <div class="fixed bottom-6 right-6 z-40 flex flex-col items-end gap-3">
    <a href="tel:0890404627" class="w-12 h-12 bg-blue-600 hover:bg-blue-500 text-white rounded-full flex items-center justify-center shadow-lg hover:scale-110 transition" title="โทรด่วน 0890404627">
      <i class="fa-solid fa-phone"></i>
    </a>
    <a href="http://line.me/ti/p/~manzx3" target="_blank" class="w-12 h-12 bg-green-500 hover:bg-green-400 text-white rounded-full flex items-center justify-center shadow-lg hover:scale-110 transition" title="LINE ID: manzx3">
      <i class="fa-brands fa-line text-2xl"></i>
    </a>
  </div>

  <!-- Article Reader Modal -->
  <div id="artModal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-3xl w-full max-h-[90vh] overflow-hidden flex flex-col shadow-2xl">
      <div class="p-4 border-b border-slate-200 flex items-center justify-between bg-slate-50">
        <span id="artModalCategory" class="px-2.5 py-0.5 text-xs font-bold bg-t2t-navy text-white rounded-full">บทความ</span>
        <button onclick="closeArtModal()" class="w-8 h-8 rounded-full bg-slate-200 hover:bg-slate-300 flex items-center justify-center">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div class="p-6 sm:p-8 overflow-y-auto space-y-4">
        <h2 id="artModalTitle" class="text-xl sm:text-2xl font-bold text-t2t-navy leading-snug"></h2>
        <div class="rounded-xl overflow-hidden max-h-64 bg-slate-100">
          <img id="artModalImg" src="" alt="" class="w-full h-full object-cover">
        </div>
        <div id="artModalBody" class="text-slate-700 text-sm font-sarabun leading-relaxed whitespace-pre-line space-y-3"></div>
      </div>
      <div class="p-4 border-t border-slate-200 bg-slate-50 flex justify-end">
        <button onclick="closeArtModal()" class="px-4 py-2 bg-t2t-navy text-white text-xs font-bold rounded-lg hover:bg-t2t-navyLight transition">
          ปิดหน้าต่าง
        </button>
      </div>
    </div>
  </div>

  <script src="articles-data.js"></script>
  <script>
    // Mobile Drawer Toggle
    document.getElementById('mobileMenuToggle').addEventListener('click', () => {
      document.getElementById('mobileDrawer').classList.toggle('hidden');
    });

    // Captcha
    let c1 = 6, c2 = 2;
    function genCaptcha() {
      c1 = Math.floor(Math.random() * 8) + 1;
      c2 = Math.floor(Math.random() * 8) + 1;
      document.getElementById('captchaText').textContent = `${c1} + ${c2} = ?`;
      document.getElementById('captchaAns').value = '';
    }

    function handleContactSubmit(e) {
      e.preventDefault();
      const ans = parseInt(document.getElementById('captchaAns').value, 10);
      if (ans !== (c1 + c2)) {
        alert('กรุณากรอกตัวเลข Captcha ให้ถูกต้อง');
        return;
      }
      alert('ข้อความของคุณถูกส่งเรียบร้อยแล้ว');
      document.getElementById('contactForm').reset();
      genCaptcha();
    }

    function handleSub(e) {
      e.preventDefault();
      alert('ได้รับข้อมูลของคุณเรียบร้อยแล้ว');
      e.target.reset();
    }

    // Article Modal Reader
    function openArticleModal(id) {
      const art = window.TEL2TELL_ARTICLES ? window.TEL2TELL_ARTICLES.find(a => a.id === id) : null;
      if (!art) return;
      document.getElementById('artModalTitle').textContent = art.title;
      document.getElementById('artModalCategory').textContent = art.category;
      document.getElementById('artModalImg').src = art.image;
      document.getElementById('artModalBody').textContent = art.content || art.excerpt;
      document.getElementById('artModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeArtModal() {
      document.getElementById('artModal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }

    genCaptcha();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_code)

print("Updated index.html to match exact original Tel2tell design and element layout!")
