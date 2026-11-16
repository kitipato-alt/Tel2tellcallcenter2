import os

html_content = """<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tel2Tell Call Center | ผู้ให้บริการ Outsource Contact Center ครบวงจร</title>
  <meta name="description" content="ผู้ให้บริการ Outsource Contact Center ครบวงจร ทั้งรับสายเข้า (Inbound) และโทรออก (Outbound Telesales) ดูแลลูกค้า 24/7 ผลิตสื่อโฆษณา VDO และระบบ Call Center Cloud มาตรฐานสากล">
  <meta name="keywords" content="Call center, Outbound Call center, Telesales, Sales Admin, VDO Production, เทล ทู เทล, tel2tell">
  
  <!-- Favicon -->
  <link rel="icon" type="image/png" href="images/logo.png">

  <!-- Google Fonts: Prompt, Sarabun, Open Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Prompt:wght@300;400;500;600;700;800&family=Sarabun:wght@300;400;500;600&display=swap" rel="stylesheet">
  
  <!-- Font Awesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Tailwind CSS CDN with custom config -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              navy: '#1B2A38',
              dark: '#111923',
              card: '#223446',
              blue: '#1C3A79',
              cyan: '#0EA5E9',
              accent: '#22D3EE',
              gold: '#F59E0B',
              goldLight: '#FEF3C7',
              line: '#00BC0C',
              surface: '#F8FAFC'
            }
          },
          fontFamily: {
            prompt: ['Prompt', 'sans-serif'],
            sarabun: ['Sarabun', 'sans-serif'],
            sans: ['Open Sans', 'Prompt', 'sans-serif']
          }
        }
      }
    }
  </script>

  <style>
    body {
      font-family: 'Prompt', 'Sarabun', sans-serif;
    }
    .glassmorphism {
      background: rgba(27, 42, 56, 0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }
    .gradient-hero {
      background: linear-gradient(135deg, rgba(17, 25, 35, 0.95) 0%, rgba(27, 42, 56, 0.88) 100%), url('images/hero-banner.jpg') center/cover no-repeat;
    }
    .text-gradient {
      background: linear-gradient(135deg, #38BDF8 0%, #22D3EE 50%, #F59E0B 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .card-hover {
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .card-hover:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 25px -5px rgba(14, 165, 233, 0.15), 0 8px 10px -6px rgba(14, 165, 233, 0.1);
    }
  </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-brand-cyan selection:text-white">

  <!-- ============================================================== -->
  <!-- TOP ANNOUNCEMENT BAR                                           -->
  <!-- ============================================================== -->
  <div class="bg-brand-dark text-slate-300 text-xs py-2 px-4 border-b border-slate-800">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-2">
      <div class="flex items-center gap-4">
        <span class="inline-flex items-center gap-1.5"><i class="fa-solid fa-phone text-brand-accent"></i> ฮอตไลน์: <a href="tel:0890404627" class="hover:text-white font-semibold">089-040-4627</a></span>
        <span class="hidden sm:inline-flex items-center gap-1.5"><i class="fa-solid fa-envelope text-brand-accent"></i> nattapon@tel2tell.com</span>
        <span class="hidden lg:inline-flex items-center gap-1.5"><i class="fa-brands fa-line text-brand-line"></i> LINE ID: manzx3</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden md:inline text-slate-400">ผู้ให้บริการ Outsource Contact Center มาตรฐานสากล ประสบการณ์กว่า 12 ปี</span>
        <div class="flex items-center gap-2 text-slate-400">
          <a href="https://www.facebook.com/Tel2tellcallcenter" target="_blank" class="hover:text-brand-accent transition"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="https://www.youtube.com/channel/UCk_17vNw0lJKEmJXoP2gyzQ" target="_blank" class="hover:text-red-400 transition"><i class="fa-brands fa-youtube"></i></a>
          <a href="http://line.me/ti/p/~manzx3" target="_blank" class="hover:text-brand-line transition"><i class="fa-brands fa-line"></i></a>
        </div>
      </div>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- NAVBAR                                                         -->
  <!-- ============================================================== -->
  <header class="sticky top-0 z-50 glassmorphism border-b border-slate-700/50 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <!-- Logo -->
        <a href="index.html" class="flex items-center gap-3 group">
          <img src="images/logo.png" alt="Tel2Tell Logo" class="h-12 w-auto object-contain rounded-lg bg-white/90 p-1 shadow-md group-hover:scale-105 transition">
          <div class="flex flex-col">
            <span class="text-xl font-bold text-white tracking-wide font-prompt">TEL2TELL</span>
            <span class="text-[11px] text-brand-accent tracking-wider font-medium">CALL CENTER & MARKETING</span>
          </div>
        </a>

        <!-- Desktop Navigation -->
        <nav class="hidden lg:flex items-center space-x-1 font-medium text-sm text-slate-200">
          <a href="index.html" class="px-3 py-2 text-white bg-slate-800/80 rounded-lg font-semibold hover:text-brand-accent transition">หน้าแรก</a>
          
          <!-- Dropdown Services -->
          <div class="relative group">
            <button class="px-3 py-2 rounded-lg hover:text-brand-accent hover:bg-slate-800/50 flex items-center gap-1.5 transition">
              <span>บริการของเรา</span>
              <i class="fa-solid fa-chevron-down text-xs text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </button>
            <div class="absolute left-0 mt-2 w-64 bg-brand-navy border border-slate-700 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 p-2 z-50">
              <a href="#services" class="flex items-center gap-3 p-2.5 rounded-lg hover:bg-slate-700/50 text-slate-200 hover:text-brand-accent transition">
                <i class="fa-solid fa-headset text-brand-cyan text-lg w-5 text-center"></i>
                <div>
                  <div class="text-sm font-semibold">Inbound Call Center</div>
                  <div class="text-xs text-slate-400">บริการรับสายและดูแลลูกค้า</div>
                </div>
              </a>
              <a href="outbound.html" class="flex items-center gap-3 p-2.5 rounded-lg hover:bg-slate-700/50 text-slate-200 hover:text-brand-accent transition">
                <i class="fa-solid fa-phone-volume text-brand-gold text-lg w-5 text-center"></i>
                <div>
                  <div class="text-sm font-semibold">Outbound Telesales</div>
                  <div class="text-xs text-slate-400">โทรออกเชิงรุก เพิ่มยอดขาย</div>
                </div>
              </a>
              <a href="sales-admin.html" class="flex items-center gap-3 p-2.5 rounded-lg hover:bg-slate-700/50 text-slate-200 hover:text-brand-accent transition">
                <i class="fa-solid fa-comments text-green-400 text-lg w-5 text-center"></i>
                <div>
                  <div class="text-sm font-semibold">Sales Admin 24/7</div>
                  <div class="text-xs text-slate-400">ตอบแชท ปิดการขายทุกช่องทาง</div>
                </div>
              </a>
              <a href="vdo-production.html" class="flex items-center gap-3 p-2.5 rounded-lg hover:bg-slate-700/50 text-slate-200 hover:text-brand-accent transition">
                <i class="fa-solid fa-video text-purple-400 text-lg w-5 text-center"></i>
                <div>
                  <div class="text-sm font-semibold">VDO Production</div>
                  <div class="text-xs text-slate-400">ผลิตสื่อสปอตทีวี & โซเชียล</div>
                </div>
              </a>
            </div>
          </div>

          <a href="outbound.html" class="px-3 py-2 rounded-lg hover:text-brand-accent hover:bg-slate-800/50 transition">Outbound</a>
          <a href="sales-admin.html" class="px-3 py-2 rounded-lg hover:text-brand-accent hover:bg-slate-800/50 transition">Sales Admin</a>
          <a href="vdo-production.html" class="px-3 py-2 rounded-lg hover:text-brand-accent hover:bg-slate-800/50 transition">VDO Production</a>
          <a href="jobs.html" class="px-3 py-2 rounded-lg hover:text-brand-accent hover:bg-slate-800/50 transition text-brand-gold font-semibold flex items-center gap-1">
            <span class="w-2 h-2 rounded-full bg-brand-gold animate-ping"></span>
            รับสมัครงาน
          </a>
          <a href="#articles" class="px-3 py-2 rounded-lg hover:text-brand-accent hover:bg-slate-800/50 transition">บทความ</a>
          <a href="#contact" class="px-3 py-2 rounded-lg hover:text-brand-accent hover:bg-slate-800/50 transition">ติดต่อเรา</a>
        </nav>

        <!-- CTA Button -->
        <div class="hidden lg:flex items-center gap-3">
          <a href="tel:0890404627" class="bg-gradient-to-r from-brand-cyan to-blue-600 hover:from-sky-400 hover:to-blue-500 text-white font-semibold text-sm px-5 py-2.5 rounded-xl shadow-lg shadow-sky-500/25 flex items-center gap-2 transition transform hover:-translate-y-0.5">
            <i class="fa-solid fa-phone"></i>
            <span>089-040-4627</span>
          </a>
        </div>

        <!-- Mobile Hamburger Button -->
        <button id="mobileMenuBtn" class="lg:hidden text-white hover:text-brand-accent p-2 rounded-lg focus:outline-none">
          <i class="fa-solid fa-bars text-2xl"></i>
        </button>
      </div>
    </div>

    <!-- Mobile Drawer -->
    <div id="mobileDrawer" class="hidden lg:hidden bg-brand-navy/95 border-b border-slate-700 px-4 pt-3 pb-6 space-y-3 font-medium text-slate-200">
      <a href="index.html" class="block px-3 py-2 rounded-lg bg-slate-800 text-white font-semibold">หน้าแรก</a>
      <a href="#services" class="block px-3 py-2 rounded-lg hover:bg-slate-800">บริการของเรา (Overview)</a>
      <a href="outbound.html" class="block px-3 py-2 rounded-lg hover:bg-slate-800">Outbound Call Center</a>
      <a href="sales-admin.html" class="block px-3 py-2 rounded-lg hover:bg-slate-800">Sales Admin</a>
      <a href="vdo-production.html" class="block px-3 py-2 rounded-lg hover:bg-slate-800">VDO Production</a>
      <a href="jobs.html" class="block px-3 py-2 rounded-lg hover:bg-slate-800 text-brand-gold font-semibold">ร่วมงานกับเรา (เปิดรับสมัคร)</a>
      <a href="#articles" class="block px-3 py-2 rounded-lg hover:bg-slate-800">บทความ</a>
      <a href="#contact" class="block px-3 py-2 rounded-lg hover:bg-slate-800">ติดต่อเรา</a>
      <div class="pt-2">
        <a href="tel:0890404627" class="w-full bg-brand-cyan text-white py-3 rounded-xl font-bold flex items-center justify-center gap-2 shadow-lg">
          <i class="fa-solid fa-phone"></i> โทรปรึกษาทันที 089-040-4627
        </a>
      </div>
    </div>
  </header>

  <!-- ============================================================== -->
  <!-- HERO BANNER                                                    -->
  <!-- ============================================================== -->
  <section class="relative gradient-hero py-20 lg:py-28 overflow-hidden text-white border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 bg-brand-cyan/20 border border-brand-cyan/40 px-3.5 py-1.5 rounded-full text-xs font-semibold text-brand-accent tracking-wide uppercase">
            <i class="fa-solid fa-shield-halved text-brand-accent"></i>
            มาตรฐานความปลอดภัยข้อมูลระดับสากล
          </div>
          
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight leading-tight">
            ผู้นำบริการ <span class="text-gradient">Outsource Contact Center</span> ครบวงจร & การตลาดระดับมืออาชีพ
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl font-sarabun">
            บริษัท เทล ทู เทล จำกัด ให้บริการทั้งรับสายเข้า (Inbound) และโทรออกเชิงรุก (Outbound Telesales) พร้อมทีมงาน Sales Admin ดูแลลูกค้า 24/7 ผลิตสื่อโฆษณา VDO Spot ทีวี และระบบ Call Center Cloud อัจฉริยะ ตอบโจทย์ทุกอุตสาหกรรม
          </p>

          <div class="flex flex-wrap items-center gap-4 pt-2">
            <a href="#contact" class="bg-gradient-to-r from-brand-cyan to-blue-600 hover:from-sky-400 hover:to-blue-500 text-white font-bold px-7 py-3.5 rounded-xl shadow-xl shadow-cyan-500/25 flex items-center gap-2 transform hover:-translate-y-0.5 transition">
              <span>ปรึกษาผู้เชี่ยวชาญ ฟรี!</span>
              <i class="fa-solid fa-arrow-right"></i>
            </a>
            <a href="#services" class="bg-slate-800/80 hover:bg-slate-700/80 border border-slate-600 text-slate-200 font-semibold px-6 py-3.5 rounded-xl flex items-center gap-2 transition">
              <i class="fa-solid fa-grid-2"></i>
              <span>ดูบริการทั้งหมด</span>
            </a>
            <a href="http://line.me/ti/p/~manzx3" target="_blank" class="bg-green-600 hover:bg-green-500 text-white font-semibold px-5 py-3.5 rounded-xl flex items-center gap-2 shadow-lg shadow-green-600/25 transition">
              <i class="fa-brands fa-line text-lg"></i>
              <span>LINE: manzx3</span>
            </a>
          </div>

          <!-- Trust Badges Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-8 border-t border-slate-700/60">
            <div class="bg-slate-800/50 backdrop-blur p-3.5 rounded-xl border border-slate-700/50">
              <div class="text-2xl font-bold text-brand-accent">12+ ปี</div>
              <div class="text-xs text-slate-400">ประสบการณ์ยาวนาน</div>
            </div>
            <div class="bg-slate-800/50 backdrop-blur p-3.5 rounded-xl border border-slate-700/50">
              <div class="text-2xl font-bold text-brand-gold">100+</div>
              <div class="text-xs text-slate-400">แบรนด์ชั้นนำไว้วางใจ</div>
            </div>
            <div class="bg-slate-800/50 backdrop-blur p-3.5 rounded-xl border border-slate-700/50">
              <div class="text-2xl font-bold text-green-400">24/7</div>
              <div class="text-xs text-slate-400">ดูแลลูกค้าตลอดเวลา</div>
            </div>
            <div class="bg-slate-800/50 backdrop-blur p-3.5 rounded-xl border border-slate-700/50">
              <div class="text-2xl font-bold text-purple-400">4 รางวัล</div>
              <div class="text-xs text-slate-400">TCCTA & เกียรติยศ</div>
            </div>
          </div>
        </div>

        <!-- Hero Card Showcase -->
        <div class="lg:col-span-5 relative">
          <div class="relative rounded-2xl overflow-hidden border border-slate-700/80 shadow-2xl bg-brand-card p-6 space-y-5">
            <div class="flex items-center justify-between border-b border-slate-700 pb-4">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-cyan-500/20 text-brand-accent flex items-center justify-center font-bold">
                  <i class="fa-solid fa-headset text-lg"></i>
                </div>
                <div>
                  <h3 class="font-bold text-white text-base">Tel2Tell Contact Suite</h3>
                  <p class="text-xs text-slate-400">All-in-one Customer Experience</p>
                </div>
              </div>
              <span class="px-2.5 py-1 text-[11px] font-semibold bg-green-500/20 text-green-400 rounded-full flex items-center gap-1">
                <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span> ระบบพร้อมทำงาน
              </span>
            </div>

            <div class="space-y-3">
              <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <i class="fa-solid fa-phone-arrow-down-left text-brand-cyan text-lg"></i>
                  <div>
                    <div class="text-sm font-semibold text-white">Inbound Call Center</div>
                    <div class="text-xs text-slate-400">รับออเดอร์, Customer Support, สายด่วน</div>
                  </div>
                </div>
                <span class="text-xs font-semibold text-cyan-300">Live Agent</span>
              </div>

              <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <i class="fa-solid fa-phone-arrow-up-right text-brand-gold text-lg"></i>
                  <div>
                    <div class="text-sm font-semibold text-white">Outbound Telesales</div>
                    <div class="text-xs text-slate-400">ปิดการขาย, ตามตะกร้า, สรุปผล Real-time</div>
                  </div>
                </div>
                <span class="text-xs font-semibold text-amber-300">CRM Auto</span>
              </div>

              <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <i class="fa-solid fa-message-dots text-emerald-400 text-lg"></i>
                  <div>
                    <div class="text-sm font-semibold text-white">Social Admin 24/7</div>
                    <div class="text-xs text-slate-400">ตอบแชท FB, LINE OA, TikTok Shop</div>
                  </div>
                </div>
                <span class="text-xs font-semibold text-emerald-300">24 ชม.</span>
              </div>

              <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <i class="fa-solid fa-server text-indigo-400 text-lg"></i>
                  <div>
                    <div class="text-sm font-semibold text-white">Cloud IP PBX System</div>
                    <div class="text-xs text-slate-400">ระบบคู่สายโทรศัพท์บันทึกเสียงและรายงาน</div>
                  </div>
                </div>
                <span class="text-xs font-semibold text-indigo-300">On Cloud</span>
              </div>
            </div>

            <div class="pt-2">
              <a href="#contact" class="w-full block text-center py-2.5 bg-brand-cyan/20 hover:bg-brand-cyan/30 text-brand-accent rounded-xl text-xs font-bold border border-brand-cyan/30 transition">
                ขอใบเสนอราคาด่วน & ประเมินระบบฟรี
              </a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 1: OUR SERVICE (4 CORE SERVICES)                       -->
  <!-- ============================================================== -->
  <section id="services" class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Title -->
      <div class="text-center max-w-3xl mx-auto space-y-4">
        <span class="text-xs font-bold tracking-wider uppercase text-brand-cyan bg-cyan-50 px-3 py-1 rounded-full border border-cyan-200">
          COMPREHENSIVE SERVICES
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy">
          Our Service (บริการหลักของเรา)
        </h2>
        <div class="w-16 h-1 bg-brand-cyan mx-auto rounded-full"></div>
        <p class="text-slate-600 text-base leading-relaxed font-sarabun">
          เรามีบริการครอบคลุมหลากหลาย พร้อมตอบรับทุกความต้องการของลูกค้าในทุกอุตสาหกรรม มุ่งมั่นและใส่ใจเต็มที่ในการทำงานเพื่อให้ได้ผลงานที่มีคุณภาพสูงสุด
        </p>
      </div>

      <!-- 4 Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mt-14">
        
        <!-- Card 1: Inbound Call Center -->
        <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden card-hover flex flex-col">
          <div class="relative h-48 overflow-hidden bg-slate-100">
            <img src="images/srv-inbound.jpg" alt="Inbound Callcenter" class="w-full h-full object-cover transform hover:scale-105 transition duration-500">
            <div class="absolute top-3 right-3 bg-brand-navy/80 backdrop-blur text-white text-xs px-2.5 py-1 rounded-full font-semibold">
              รับสายเข้า
            </div>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="w-10 h-10 rounded-xl bg-cyan-50 text-brand-cyan flex items-center justify-center font-bold mb-3">
                <i class="fa-solid fa-headset text-xl"></i>
              </div>
              <h3 class="text-xl font-bold text-brand-navy">Inbound Callcenter</h3>
              <p class="text-slate-600 text-sm mt-2 font-sarabun leading-relaxed">
                บริการรับสายโทรเข้า บริการข้อมูลสินค้าและบริการ รับสั่งซื้อสินค้า จัดการเรื่องร้องเรียน พร้อมระบบบันทึกเสียงและวัดผลความพึงพอใจ
              </p>
            </div>
            <ul class="text-xs text-slate-500 space-y-1.5 pt-2 border-t border-slate-100 font-sarabun">
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> รับเรื่องและให้ข้อมูล 24 ชั่วโมง</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> สรุปรายงานเคสและ SLA แม่นยำ</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> เจ้าหน้าที่ผ่านการอบรมมารยาท</li>
            </ul>
            <a href="#contact" class="mt-4 inline-flex items-center text-sm font-semibold text-brand-cyan hover:text-sky-700">
              ขอข้อมูลบริการ <i class="fa-solid fa-arrow-right ml-1.5 text-xs"></i>
            </a>
          </div>
        </div>

        <!-- Card 2: Outbound Call Center -->
        <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden card-hover flex flex-col">
          <div class="relative h-48 overflow-hidden bg-slate-100">
            <img src="images/srv-outbound.jpg" alt="Outbound Callcenter" class="w-full h-full object-cover transform hover:scale-105 transition duration-500">
            <div class="absolute top-3 right-3 bg-brand-gold/90 text-white text-xs px-2.5 py-1 rounded-full font-semibold">
              โทรออกเชิงรุก
            </div>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="w-10 h-10 rounded-xl bg-amber-50 text-brand-gold flex items-center justify-center font-bold mb-3">
                <i class="fa-solid fa-phone-volume text-xl"></i>
              </div>
              <h3 class="text-xl font-bold text-brand-navy">Outbound Callcenter</h3>
              <p class="text-slate-600 text-sm mt-2 font-sarabun leading-relaxed">
                บริการโทรออกนำเสนอขายสินค้า (Telesales) โทรติดตามลูกค้าเก่า โทรแจ้งโปรโมชั่นพิเศษ และโทรสำรวจความพึงพอใจอย่างมืออาชีพ
              </p>
            </div>
            <ul class="text-xs text-slate-500 space-y-1.5 pt-2 border-t border-slate-100 font-sarabun">
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> ทีม Telesales เชี่ยวชาญการปิดการขาย</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> บันทึกข้อมูลลง CRM ทุกสาย</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> รายงานยอดขายและผลตอบรับ Real-time</li>
            </ul>
            <a href="outbound.html" class="mt-4 inline-flex items-center text-sm font-semibold text-brand-cyan hover:text-sky-700">
              ดูรายละเอียด Outbound <i class="fa-solid fa-arrow-right ml-1.5 text-xs"></i>
            </a>
          </div>
        </div>

        <!-- Card 3: Social Media Support -->
        <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden card-hover flex flex-col">
          <div class="relative h-48 overflow-hidden bg-slate-100">
            <img src="images/srv-social.jpg" alt="Social Media Support" class="w-full h-full object-cover transform hover:scale-105 transition duration-500">
            <div class="absolute top-3 right-3 bg-emerald-600 text-white text-xs px-2.5 py-1 rounded-full font-semibold">
              แอดมินตอบแชท
            </div>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold mb-3">
                <i class="fa-solid fa-comments text-xl"></i>
              </div>
              <h3 class="text-xl font-bold text-brand-navy">Social Media Support</h3>
              <p class="text-slate-600 text-sm mt-2 font-sarabun leading-relaxed">
                บริการแอดมินตอบข้อความทุกแพลตฟอร์ม Facebook, LINE Official, TikTok, Shopee, Lazada ดูแลลูกค้า 24 ชม. ปิดการขายไว
              </p>
            </div>
            <ul class="text-xs text-slate-500 space-y-1.5 pt-2 border-t border-slate-100 font-sarabun">
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> ตอบกลับภายใน 1-3 นาที</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> สคริปต์ปิดการขายเฉพาะธุรกิจ</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> คีย์ออเดอร์และประสานงานจัดส่ง</li>
            </ul>
            <a href="sales-admin.html" class="mt-4 inline-flex items-center text-sm font-semibold text-brand-cyan hover:text-sky-700">
              ดูรายละเอียด Sales Admin <i class="fa-solid fa-arrow-right ml-1.5 text-xs"></i>
            </a>
          </div>
        </div>

        <!-- Card 4: Onsite Service -->
        <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden card-hover flex flex-col">
          <div class="relative h-48 overflow-hidden bg-slate-100">
            <img src="images/srv-onsite.jpg" alt="Onsite Service" class="w-full h-full object-cover transform hover:scale-105 transition duration-500">
            <div class="absolute top-3 right-3 bg-purple-600 text-white text-xs px-2.5 py-1 rounded-full font-semibold">
              บริการนอกสถานที่
            </div>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center font-bold mb-3">
                <i class="fa-solid fa-users-gear text-xl"></i>
              </div>
              <h3 class="text-xl font-bold text-brand-navy">Onsite Service</h3>
              <p class="text-slate-600 text-sm mt-2 font-sarabun leading-relaxed">
                บริการจัดส่งทีมงาน Call Center และเจ้าหน้าที่สนับสนุนไปปฏิบัติงาน ณ สำนักงานของลูกค้า บริหารจัดการครบวงจร
              </p>
            </div>
            <ul class="text-xs text-slate-500 space-y-1.5 pt-2 border-t border-slate-100 font-sarabun">
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> คัดสรรบุคลากรตรงตามสเปก</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> ดูแลสวัสดิการและประกันสังคมครบ</li>
              <li><i class="fa-solid fa-check text-green-500 mr-1.5"></i> มี Supervisor ควบคุมคุณภาพงาน</li>
            </ul>
            <a href="#contact" class="mt-4 inline-flex items-center text-sm font-semibold text-brand-cyan hover:text-sky-700">
              ปรึกษาทีม Onsite <i class="fa-solid fa-arrow-right ml-1.5 text-xs"></i>
            </a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 2: MEDIA, TV SPOT & CLOUD PBX                          -->
  <!-- ============================================================== -->
  <section class="py-16 bg-slate-50 border-y border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto space-y-3 mb-12">
        <span class="text-xs font-bold uppercase tracking-wider text-brand-gold bg-amber-50 px-3 py-1 rounded-full border border-amber-200">
          MEDIA & TECHNOLOGY
        </span>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-brand-navy">
          บริการสื่อโฆษณาโทรทัศน์ & ระบบ Call Center Cloud
        </h2>
        <div class="w-12 h-1 bg-brand-gold mx-auto rounded-full"></div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Media Card 1 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-6 card-hover flex flex-col justify-between">
          <div class="space-y-4">
            <div class="h-44 rounded-xl overflow-hidden bg-slate-100">
              <img src="images/srv-spot-ads.jpg" alt="รับผลิตสื่อโฆษณา Spot" class="w-full h-full object-cover">
            </div>
            <h3 class="text-lg font-bold text-brand-navy">รับผลิตสื่อโฆษณา Spot ทุกประเภทสินค้า</h3>
            <p class="text-slate-600 text-sm font-sarabun leading-relaxed">
              บริการผลิตสปอตโฆษณา วิดีโอพรีเซนเทชัน พร้อมดำเนินการ **ยื่นตรวจพิจารณาสื่อ (Censored)** สำหรับออกอากาศทางสถานีโทรทัศน์ถูกต้องตามกฎหมาย
            </p>
          </div>
          <a href="vdo-production.html" class="mt-6 inline-flex items-center text-sm font-semibold text-brand-cyan hover:text-sky-700">
            ดูงาน VDO Production <i class="fa-solid fa-arrow-right ml-1.5 text-xs"></i>
          </a>
        </div>

        <!-- Media Card 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-6 card-hover flex flex-col justify-between">
          <div class="space-y-4">
            <div class="h-44 rounded-xl overflow-hidden bg-slate-100">
              <img src="images/srv-tv-air.jpg" alt="ลงสื่อโฆษณาทางทีวี" class="w-full h-full object-cover">
            </div>
            <h3 class="text-lg font-bold text-brand-navy">เพิ่มยอดขายช่องทางออฟไลน์ ลงสื่อโฆษณาทางทีวี</h3>
            <p class="text-slate-600 text-sm font-sarabun leading-relaxed">
              วางแผนและซื้อเวลาโฆษณาโทรทัศน์ ดิจิทัลทีวี และรายการแนะนำสินค้า สร้างความน่าเชื่อถือให้แบรนด์ เข้าถึงกลุ่มลูกค้าระดับประเทศ พร้อมทีมรับสาย Call Center รองรับคำสั่งซื้อ
            </p>
          </div>
          <a href="#contact" class="mt-6 inline-flex items-center text-sm font-semibold text-brand-cyan hover:text-sky-700">
            สอบถามแพ็กเกจทีวี <i class="fa-solid fa-arrow-right ml-1.5 text-xs"></i>
          </a>
        </div>

        <!-- Media Card 3 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-6 card-hover flex flex-col justify-between">
          <div class="space-y-4">
            <div class="h-44 rounded-xl overflow-hidden bg-slate-100">
              <img src="images/srv-cloud-pbx.jpg" alt="ระบบ Call Center IP PBX" class="w-full h-full object-cover">
            </div>
            <h3 class="text-lg font-bold text-brand-navy">ระบบ Call Center IP PBX & Cloud On Demand</h3>
            <p class="text-slate-600 text-sm font-sarabun leading-relaxed">
              ติดตั้งและให้เช่าระบบ Call Center Cloud บันทึกเสียงทุกคู่สาย ดึงสถิติวิเคราะห์ IVR ระบบกระจายสายอัตโนมัติ และเชื่อมต่อระบบ CRM ขององค์กรได้อย่างสมบูรณ์แบบ
            </p>
          </div>
          <a href="#contact" class="mt-6 inline-flex items-center text-sm font-semibold text-brand-cyan hover:text-sky-700">
            ปรึกษาระบบ Cloud PBX <i class="fa-solid fa-arrow-right ml-1.5 text-xs"></i>
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 3: 12 YEARS EXPERIENCE & 6 CORE CAPABILITIES           -->
  <!-- ============================================================== -->
  <section class="py-20 bg-brand-navy text-white relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Experience Header -->
      <div class="text-center max-w-3xl mx-auto space-y-4">
        <div class="inline-flex items-center gap-2 bg-brand-gold/20 border border-brand-gold/40 px-3.5 py-1.5 rounded-full text-xs font-semibold text-brand-gold uppercase tracking-wider">
          <i class="fa-solid fa-award"></i>
          ESTABLISHED SINCE 2012
        </div>
        <h2 class="text-3xl sm:text-5xl font-extrabold tracking-tight">
          12 Years Experience
        </h2>
        <div class="w-20 h-1 bg-brand-cyan mx-auto rounded-full"></div>
        <p class="text-slate-300 text-base sm:text-lg leading-relaxed font-sarabun">
          เราเป็นผู้ให้บริการด้าน **Outsource Contact Center และการตลาดครบวงจร** รวมถึงบริการด้านการขาย การสร้างความสัมพันธ์กับลูกค้าช่องทางออนไลน์และออฟไลน์ งานคอลเซ็นเตอร์ ระบบคอลเซ็นเตอร์ งานโปรดักชั่น สื่อโฆษณาทางโทรทัศน์ และคลังสินค้า
        </p>
      </div>

      <!-- 6 Capabilities Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-16">
        
        <!-- Cap 1 -->
        <div class="bg-brand-card/90 border border-slate-700/80 rounded-2xl p-6 card-hover space-y-4">
          <div class="h-40 rounded-xl overflow-hidden bg-slate-800">
            <img src="images/cap-outsource.jpg" alt="Outsource Service Center" class="w-full h-full object-cover">
          </div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-building-user text-brand-cyan"></i>
            Outsource Service Center
          </h3>
          <p class="text-slate-300 text-sm font-sarabun leading-relaxed">
            ศูนย์บริการลูกค้าสัมพันธ์แบบเบ็ดเสร็จ ลดต้นทุนการจ้างงานและการบริหาร ลดภาระการเทรนนิ่งคน พร้อมส่งมอบบริการคุณภาพ
          </p>
        </div>

        <!-- Cap 2 -->
        <div class="bg-brand-card/90 border border-slate-700/80 rounded-2xl p-6 card-hover space-y-4">
          <div class="h-40 rounded-xl overflow-hidden bg-slate-800">
            <img src="images/cap-pbx.jpg" alt="ระบบ Call center" class="w-full h-full object-cover">
          </div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-network-wired text-brand-gold"></i>
            ระบบ Call Center
          </h3>
          <p class="text-slate-300 text-sm font-sarabun leading-relaxed">
            ระบบโครงสร้างพื้นฐานคู่สายและซอฟต์แวร์ Contact Center มาตรฐานสูง รองรับการโทรพร้อมกันจำนวนมากแบบไม่มีสะดุด
          </p>
        </div>

        <!-- Cap 3 -->
        <div class="bg-brand-card/90 border border-slate-700/80 rounded-2xl p-6 card-hover space-y-4">
          <div class="h-40 rounded-xl overflow-hidden bg-slate-800">
            <img src="images/cap-tv.jpg" alt="สื่อโฆษณาทางโทรทัศน์" class="w-full h-full object-cover">
          </div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-tv text-purple-400"></i>
            สื่อโฆษณาทางโทรทัศน์
          </h3>
          <p class="text-slate-300 text-sm font-sarabun leading-relaxed">
            เชื่อมโยงการตลาดผ่านหน้าจอทีวีดิจิทัล เข้าถึงกลุ่มเป้าหมายวงกว้าง สร้างยอดขายและการรับรู้ในระดับมวลชน
          </p>
        </div>

        <!-- Cap 4 -->
        <div class="bg-brand-card/90 border border-slate-700/80 rounded-2xl p-6 card-hover space-y-4">
          <div class="h-40 rounded-xl overflow-hidden bg-slate-800">
            <img src="images/cap-import-export.jpg" alt="Import & Export" class="w-full h-full object-cover">
          </div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-plane-departure text-green-400"></i>
            Import & Export
          </h3>
          <p class="text-slate-300 text-sm font-sarabun leading-relaxed">
            การสนับสนุนด้านการค้าระหว่างประเทศ ช่วยประสานงานการนำเข้า-ส่งออกสินค้า ตอบสนองความต้องการลูกค้าระดับสากล
          </p>
        </div>

        <!-- Cap 5 -->
        <div class="bg-brand-card/90 border border-slate-700/80 rounded-2xl p-6 card-hover space-y-4">
          <div class="h-40 rounded-xl overflow-hidden bg-slate-800">
            <img src="images/cap-data-analysis.jpg" alt="Data Analysis" class="w-full h-full object-cover">
          </div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-chart-pie text-sky-400"></i>
            Data Analysis
          </h3>
          <p class="text-slate-300 text-sm font-sarabun leading-relaxed">
            วิเคราะห์พฤติกรรมลูกค้าจากสถิติการโทรและแชท เจาะลึกความพึงพอใจเพื่อนำไปพัฒนาแผนการตลาดและเพิ่มอัตราซื้อซ้ำ
          </p>
        </div>

        <!-- Cap 6 -->
        <div class="bg-brand-card/90 border border-slate-700/80 rounded-2xl p-6 card-hover space-y-4">
          <div class="h-40 rounded-xl overflow-hidden bg-slate-800">
            <img src="images/cap-fulfillment.jpg" alt="Fulfillment" class="w-full h-full object-cover">
          </div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-boxes-packing text-amber-400"></i>
            Fulfillment & Warehousing
          </h3>
          <p class="text-slate-300 text-sm font-sarabun leading-relaxed">
            บริการคลังสินค้า จัดเก็บ แพ็ค ส่ง ร่วมกับบริษัทในเครือ (FG Logistics) เชื่อมต่อระบบสต๊อกและการส่งมอบทันที
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 4: OUR CLIENTS                                         -->
  <!-- ============================================================== -->
  <section class="py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
      
      <div class="space-y-2">
        <span class="text-xs font-bold uppercase tracking-wider text-slate-400">TRUSTED BY LEADING BRANDS</span>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-brand-navy">Our Clients</h2>
        <p class="text-slate-600 text-sm font-sarabun">ขอขอบคุณลูกค้าที่วางใจและใช้บริการ บริษัท เทล ทู เทล จำกัด</p>
      </div>

      <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 lg:p-10 shadow-sm max-w-5xl mx-auto">
        <img src="images/client-logos.jpg" alt="Our Clients" class="w-full h-auto object-contain mx-auto rounded-lg">
      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 5: PERFORMANCE, AWARDS & CSR                           -->
  <!-- ============================================================== -->
  <section class="py-20 bg-slate-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto space-y-4 mb-14">
        <span class="text-xs font-bold uppercase tracking-wider text-brand-gold bg-amber-50 px-3 py-1 rounded-full border border-amber-200">
          ACHIEVEMENTS & SOCIAL CONTRIBUTION
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy">
          Performance & CSR Awards
        </h2>
        <div class="w-16 h-1 bg-brand-gold mx-auto rounded-full"></div>
        <p class="text-slate-600 text-sm sm:text-base font-sarabun leading-relaxed">
          ความภาคภูมิใจในผลงานและการช่วยเหลือสังคม บริษัท เทล ทู เทล จำกัด ได้รับรางวัลเกียรติยศระดับประเทศ และร่วมมือกับภาครัฐในสถานการณ์วิกฤต
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Award 1 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm card-hover flex flex-col justify-between">
          <div class="space-y-3">
            <div class="h-44 rounded-xl overflow-hidden bg-slate-100">
              <img src="images/award-1668.jpg" alt="สายด่วน 1668" class="w-full h-full object-cover">
            </div>
            <span class="px-2.5 py-1 text-[11px] font-bold bg-blue-50 text-blue-600 rounded-full inline-block">
              CSR กรมการแพทย์
            </span>
            <h4 class="font-bold text-brand-navy text-sm leading-snug">
              สนับสนุนและร่วมมือเป็น Call Center ศูนย์ประสานงานจัดหาเตียง สายด่วน 1668
            </h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              ร่วมมือกับกรมการแพทย์ในวิกฤตโควิด-19 นำทีมคอลเซ็นเตอร์ช่วยเหลือผู้ป่วยตลอด 24 ชั่วโมง
            </p>
          </div>
        </div>

        <!-- Award 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm card-hover flex flex-col justify-between">
          <div class="space-y-3">
            <div class="h-44 rounded-xl overflow-hidden bg-slate-100">
              <img src="images/award-tccta-gold.jpg" alt="TCCTA Gold Award" class="w-full h-full object-cover">
            </div>
            <span class="px-2.5 py-1 text-[11px] font-bold bg-amber-50 text-amber-700 rounded-full inline-block">
              TCCTA GOLD AWARD
            </span>
            <h4 class="font-bold text-brand-navy text-sm leading-snug">
              The Best Corporate Social Responsibility Award
            </h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              รางวัลชนะเลิศเหรียญทอง ด้านความรับผิดชอบต่อสังคมและสิ่งแวดล้อม จากสมาคมคอนแทคเซ็นเตอร์ไทย
            </p>
          </div>
        </div>

        <!-- Award 3 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm card-hover flex flex-col justify-between">
          <div class="space-y-3">
            <div class="h-44 rounded-xl overflow-hidden bg-slate-100">
              <img src="images/award-tccta-covid.jpg" alt="TCCTA Covid Award" class="w-full h-full object-cover">
            </div>
            <span class="px-2.5 py-1 text-[11px] font-bold bg-green-50 text-green-700 rounded-full inline-block">
              TCCTA HONOR AWARD
            </span>
            <h4 class="font-bold text-brand-navy text-sm leading-snug">
              ผู้ให้การสนับสนุนโครงการรับเรื่องและช่วยเหลือผู้ป่วยโควิด-19
            </h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              เชิดชูเกียรติองค์กรที่เป็นเสาหลักในการประสานงานช่วยเหลือประชาชนอย่างเต็มกำลัง
            </p>
          </div>
        </div>

        <!-- Award 4 / Atmosphere -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm card-hover flex flex-col justify-between">
          <div class="space-y-3">
            <div class="h-44 rounded-xl overflow-hidden bg-slate-100">
              <img src="images/atmosphere.gif" alt="ภาพบรรยากาศการทำงาน" class="w-full h-full object-cover">
            </div>
            <span class="px-2.5 py-1 text-[11px] font-bold bg-purple-50 text-purple-700 rounded-full inline-block">
              TEAM ATMOSPHERE
            </span>
            <h4 class="font-bold text-brand-navy text-sm leading-snug">
              ภาพบรรยากาศการทำงานจริง & การฝึกอบรม
            </h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              ศูนย์ปฏิบัติการมาตรฐานสูง สภาพแวดล้อมการทำงานอบอุ่น มีการเทรนนิ่งพัฒนาบุคลากรอย่างต่อเนื่อง
            </p>
          </div>
        </div>

      </div>

      <!-- Affiliate Partner Banner -->
      <div class="mt-12 bg-white rounded-2xl border border-slate-200 p-6 lg:p-8 flex flex-col md:flex-row items-center justify-between gap-6 shadow-sm">
        <div class="flex items-center gap-4">
          <img src="images/dhipaya-training.png" alt="Dhipaya Training Center" class="h-16 w-auto object-contain">
          <div>
            <h3 class="font-bold text-brand-navy text-base sm:text-lg">ศูนย์ฝึกอบรมพันธมิตรคุณภาพ</h3>
            <p class="text-xs text-slate-500 font-sarabun">พัฒนาทักษะพนักงานด้วยหลักสูตรมาตรฐานสากล ร่วมกับ Dhipaya Training</p>
          </div>
        </div>
        <a href="https://www.dhipaya-training.com/" target="_blank" class="px-5 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-xl border border-slate-300 transition">
          เยี่ยมชมศูนย์ฝึกอบรม <i class="fa-solid fa-arrow-up-right-from-square ml-1"></i>
        </a>
      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 6: WHY US                                              -->
  <!-- ============================================================== -->
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-5 space-y-6">
          <span class="text-xs font-bold uppercase tracking-wider text-brand-cyan bg-cyan-50 px-3 py-1 rounded-full border border-cyan-200">
            WHY TEL2TELL
          </span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy leading-tight">
            ทำไมธุรกิจชั้นนำถึงไว้วางใจเลือก "เทล ทู เทล"
          </h2>
          <div class="w-16 h-1 bg-brand-cyan rounded-full"></div>
          <p class="text-slate-600 text-base leading-relaxed font-sarabun">
            เราไม่ใช่แค่ผู้ให้บริการ Call Center แต่เราคือคู่คิดทางธุรกิจ (Business Partner) ที่พร้อมช่วยผลักดันยอดขาย ดูแลฐานลูกค้า และลดภาระการบริหารจัดการขององค์กรคุณอย่างมีประสิทธิภาพ
          </p>
          <div class="pt-2">
            <a href="#contact" class="inline-flex items-center gap-2 bg-brand-navy hover:bg-slate-800 text-white font-bold text-sm px-6 py-3.5 rounded-xl shadow-lg transition">
              <i class="fa-solid fa-comments"></i>
              <span>เริ่มต้นปรึกษาเราวันนี้</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-5">
          
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 card-hover space-y-2">
            <div class="w-9 h-9 rounded-lg bg-cyan-100 text-brand-cyan flex items-center justify-center font-bold">
              <i class="fa-solid fa-certificate"></i>
            </div>
            <h4 class="font-bold text-brand-navy text-sm">บริการคุณภาพมาตรฐานสากล</h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              การบริหารจัดการที่มีระบบ มีกระบวนการตรวจสอบคุณภาพเสียง (QA) และรายงาน SLA ชัดเจน
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 card-hover space-y-2">
            <div class="w-9 h-9 rounded-lg bg-green-100 text-green-600 flex items-center justify-center font-bold">
              <i class="fa-solid fa-lock"></i>
            </div>
            <h4 class="font-bold text-brand-navy text-sm">นโยบายความปลอดภัยข้อมูลเข้มงวด</h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              ปฏิบัติตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA) พร้อมระบบรักษาความปลอดภัยระดับสูง
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 card-hover space-y-2">
            <div class="w-9 h-9 rounded-lg bg-amber-100 text-brand-gold flex items-center justify-center font-bold">
              <i class="fa-solid fa-layer-group"></i>
            </div>
            <h4 class="font-bold text-brand-navy text-sm">ความเชี่ยวชาญหลากอุตสาหกรรม</h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              ครอบคลุมทั้ง E-commerce, สินค้าสุขภาพและความงาม, ประกันภัย, อสังหาฯ และยานยนต์
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 card-hover space-y-2">
            <div class="w-9 h-9 rounded-lg bg-purple-100 text-purple-600 flex items-center justify-center font-bold">
              <i class="fa-solid fa-truck-fast"></i>
            </div>
            <h4 class="font-bold text-brand-navy text-sm">บริการครบวงจร โลจิสติกส์ & คลัง</h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              ดูแลตั้งแต่การรับสาย การปิดยอดขาย ไปจนถึงการแพ็ค จัดเก็บ และส่งมอบพัสดุ
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 card-hover space-y-2">
            <div class="w-9 h-9 rounded-lg bg-blue-100 text-blue-600 flex items-center justify-center font-bold">
              <i class="fa-solid fa-laptop-code"></i>
            </div>
            <h4 class="font-bold text-brand-navy text-sm">ระบบจัดการออเดอร์ที่สะดวกสบาย</h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              เชื่อมต่อระบบ Order Management System (OMS) ตรวจสอบสถานะการสั่งซื้อได้ตลอด 24 ชั่วโมง
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 card-hover space-y-2">
            <div class="w-9 h-9 rounded-lg bg-rose-100 text-rose-600 flex items-center justify-center font-bold">
              <i class="fa-solid fa-hand-holding-heart"></i>
            </div>
            <h4 class="font-bold text-brand-navy text-sm">ปรึกษาการตลาด ออฟไลน์ & ออนไลน์ ฟรี</h4>
            <p class="text-xs text-slate-500 font-sarabun leading-relaxed">
              ให้คำแนะนำด้านการยิงแอด การลงสปอตทีวี และการวางกลยุทธ์สร้างยอดขายแบบไม่คิดค่าใช้จ่าย
            </p>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 7: ARTICLES & KNOWLEDGE HUB                            -->
  <!-- ============================================================== -->
  <section id="articles" class="py-20 bg-slate-50 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Title & Filter -->
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10">
        <div class="space-y-3">
          <span class="text-xs font-bold uppercase tracking-wider text-brand-cyan bg-cyan-50 px-3 py-1 rounded-full border border-cyan-200">
            KNOWLEDGE & INSIGHTS
          </span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy">
            บทความ & ข่าวสารล่าสุด
          </h2>
          <p class="text-slate-600 text-sm font-sarabun max-w-xl">
            เจาะลึกเทคนิคการเพิ่มยอดขายด้วย Call Center, เคล็ดลับงาน Telesales, การผลิตวิดีโอ VDO Production และข่าวสารความเคลื่อนไหว
          </p>
        </div>

        <!-- Search Bar -->
        <div class="relative w-full md:w-72">
          <input type="text" id="articleSearchInput" placeholder="ค้นหาบทความ..." class="w-full bg-white border border-slate-300 rounded-xl pl-10 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan focus:border-transparent">
          <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3 text-slate-400 text-xs"></i>
        </div>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex items-center gap-2 overflow-x-auto pb-4 scrollbar-none text-xs font-semibold" id="categoryFilters">
        <button class="cat-filter-btn px-4 py-2 rounded-full bg-brand-navy text-white transition active" data-cat="all">
          ทั้งหมด (65)
        </button>
        <button class="cat-filter-btn px-4 py-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:border-brand-cyan transition" data-cat="VDO & Production">
          VDO & Production (9)
        </button>
        <button class="cat-filter-btn px-4 py-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:border-brand-cyan transition" data-cat="Telesales & Outbound">
          Telesales & Outbound (7)
        </button>
        <button class="cat-filter-btn px-4 py-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:border-brand-cyan transition" data-cat="Call Center Knowledge">
          Call Center Knowledge (24)
        </button>
        <button class="cat-filter-btn px-4 py-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:border-brand-cyan transition" data-cat="CSR & Company">
          รางวัล & กิจกรรม (13)
        </button>
      </div>

      <!-- Articles Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-6" id="articlesGrid">
        <!-- Generated by JavaScript -->
      </div>

      <!-- View More Button -->
      <div class="text-center mt-12">
        <button id="viewAllArticlesBtn" class="bg-white border-2 border-brand-navy hover:bg-brand-navy hover:text-white text-brand-navy font-bold text-sm px-8 py-3 rounded-xl shadow-sm transition">
          ดูบทความทั้งหมดในคลัง (65 บทความ)
        </button>
      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 8: WORK WITH US (CAREERS)                              -->
  <!-- ============================================================== -->
  <section class="py-20 bg-brand-navy text-white relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto space-y-4 mb-14">
        <span class="text-xs font-bold uppercase tracking-wider text-brand-gold bg-amber-400/20 px-3 py-1 rounded-full border border-amber-400/30">
          JOIN OUR PASSIONATE TEAM
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight">
          Work With Us (ร่วมงานกับเรา)
        </h2>
        <div class="w-16 h-1 bg-brand-cyan mx-auto rounded-full"></div>
        <p class="text-slate-300 text-sm sm:text-base font-sarabun leading-relaxed">
          ร่วมเป็นส่วนหนึ่งของครอบครัว Tel2Tell และเครือ SE BIZ Group เติบโตไปพร้อมกับทีมงานมืออาชีพ บรรยากาศอบอุ่น มั่นคง และสวัสดิการครบครัน
        </p>
      </div>

      <!-- Embedded Video Presentation -->
      <div class="max-w-4xl mx-auto rounded-2xl overflow-hidden shadow-2xl border border-slate-700 bg-black aspect-video mb-16">
        <iframe class="w-full h-full" src="https://www.youtube.com/embed/tcVvzUBzVmQ" title="Tel2Tell Work With Us Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>

      <!-- 3 Job Openings Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Job 1: Telesales -->
        <div class="bg-brand-card/90 rounded-2xl border border-slate-700 p-6 flex flex-col justify-between space-y-6 card-hover">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="px-2.5 py-1 text-xs font-bold bg-amber-500/20 text-brand-gold rounded-full">รายได้รวม 15,000 - 40,000+</span>
              <span class="text-xs text-slate-400">หลายอัตรา</span>
            </div>
            <h3 class="text-xl font-bold text-white">Telesales (พนักงานขายทางโทรศัพท์)</h3>
            <p class="text-slate-300 text-xs font-sarabun leading-relaxed">
              นำเสนอขายสินค้าและโปรโมชั่นพิเศษแก่ลูกค้าทางโทรศัพท์ มีฐานรายชื่อลูกค้าให้พร้อม ไม่ต้องหาลูกค้าเอง
            </p>
            <div class="text-xs text-slate-300 space-y-1 font-sarabun">
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> วุฒิ ม.3 ขึ้นไป / อายุ 18-40 ปี</div>
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> เงินเดือนประจำ + คอมมิชชั่นสูง</div>
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> มีการอบรมเทคนิคการขายให้ฟรี</div>
            </div>
          </div>
          <button onclick="openJobModal('Telesales (พนักงานขายทางโทรศัพท์)')" class="w-full py-2.5 bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold text-sm rounded-xl transition">
            สมัครตำแหน่งนี้
          </button>
        </div>

        <!-- Job 2: Admin -->
        <div class="bg-brand-card/90 rounded-2xl border border-slate-700 p-6 flex flex-col justify-between space-y-6 card-hover">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="px-2.5 py-1 text-xs font-bold bg-emerald-500/20 text-emerald-400 rounded-full">เงินเดือนประจำ + เบี้ยขยัน</span>
              <span class="text-xs text-slate-400">หลายอัตรา</span>
            </div>
            <h3 class="text-xl font-bold text-white">Admin (แอดมินเพจ / ตอบแชท)</h3>
            <p class="text-slate-300 text-xs font-sarabun leading-relaxed">
              ตอบคำถาม ให้ข้อมูล แนะนำสินค้า และรับคำสั่งซื้อผ่าน Facebook, LINE Official, TikTok ปิดการขายทางแชท
            </p>
            <div class="text-xs text-slate-300 space-y-1 font-sarabun">
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> พิมพ์เร็ว สื่อสารรู้เรื่อง มีไหวพริบ</div>
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> ใช้คอมพิวเตอร์และสมาร์ตโฟนคล่อง</div>
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> มีสวัสดิการและประกันสังคม</div>
            </div>
          </div>
          <button onclick="openJobModal('Admin (แอดมินเพจ / ตอบแชท)')" class="w-full py-2.5 bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold text-sm rounded-xl transition">
            สมัครตำแหน่งนี้
          </button>
        </div>

        <!-- Job 3: Call Center TV -->
        <div class="bg-brand-card/90 rounded-2xl border border-slate-700 p-6 flex flex-col justify-between space-y-6 card-hover">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="px-2.5 py-1 text-xs font-bold bg-purple-500/20 text-purple-300 rounded-full">รายได้รวม 11,000 + คอม</span>
              <span class="text-xs text-slate-400">ทำเป็นกะ</span>
            </div>
            <h3 class="text-xl font-bold text-white">Callcenter TV (รับสายรายการทีวี)</h3>
            <p class="text-slate-300 text-xs font-sarabun leading-relaxed">
              รับสายและจำหน่ายสินค้าในรายการโทรทัศน์ ช่วงเวลา 09.00 - 23.00 น. มีสคริปต์สินค้าให้พร้อม สัมภาษณ์ทราบผลทันที
            </p>
            <div class="text-xs text-slate-300 space-y-1 font-sarabun">
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> วุฒิ ม.3 ขึ้นไป / อายุ 18-40 ปี</div>
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> รับแรงกดดันได้ดี พร้อมเริ่มงานทันที</div>
              <div><i class="fa-solid fa-check text-brand-accent mr-1"></i> มีโบนัสยอดขายพิเศษประจำเดือน</div>
            </div>
          </div>
          <button onclick="openJobModal('Callcenter TV (รับสายรายการทีวี)')" class="w-full py-2.5 bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold text-sm rounded-xl transition">
            สมัครตำแหน่งนี้
          </button>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SECTION 9: CONTACT US                                          -->
  <!-- ============================================================== -->
  <section id="contact" class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto space-y-3 mb-14">
        <span class="text-xs font-bold uppercase tracking-wider text-brand-cyan bg-cyan-50 px-3 py-1 rounded-full border border-cyan-200">
          GET IN TOUCH
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-navy">
          Contact Us (ติดต่อเรา)
        </h2>
        <div class="w-16 h-1 bg-brand-cyan mx-auto rounded-full"></div>
        <p class="text-slate-600 text-sm font-sarabun">
          สนใจบริการ Outsource Contact Center, สื่อโฆษณา หรือระบบ Call Center ติดต่อทีมงานผู้เชี่ยวชาญได้ทันที
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        
        <!-- Contact Information Cards -->
        <div class="lg:col-span-5 space-y-6">
          
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 space-y-4">
            <h3 class="text-lg font-bold text-brand-navy">ช่องทางติดต่อด่วน</h3>
            
            <a href="tel:0890404627" class="flex items-center gap-4 p-3 rounded-xl bg-white border border-slate-200/80 hover:border-brand-cyan transition group">
              <div class="w-11 h-11 rounded-xl bg-cyan-50 text-brand-cyan flex items-center justify-center font-bold text-lg group-hover:scale-105 transition">
                <i class="fa-solid fa-phone"></i>
              </div>
              <div>
                <div class="text-xs text-slate-500">โทรศัพท์สายด่วน</div>
                <div class="text-base font-bold text-brand-navy group-hover:text-brand-cyan transition">089-040-4627</div>
              </div>
            </a>

            <a href="mailto:nattapon@tel2tell.com" class="flex items-center gap-4 p-3 rounded-xl bg-white border border-slate-200/80 hover:border-brand-cyan transition group">
              <div class="w-11 h-11 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-lg group-hover:scale-105 transition">
                <i class="fa-solid fa-envelope"></i>
              </div>
              <div>
                <div class="text-xs text-slate-500">อีเมลติดต่อ</div>
                <div class="text-sm font-bold text-brand-navy group-hover:text-blue-600 transition">nattapon@tel2tell.com</div>
              </div>
            </a>

            <a href="http://line.me/ti/p/~manzx3" target="_blank" class="flex items-center gap-4 p-3 rounded-xl bg-white border border-slate-200/80 hover:border-green-500 transition group">
              <div class="w-11 h-11 rounded-xl bg-green-50 text-green-600 flex items-center justify-center font-bold text-xl group-hover:scale-105 transition">
                <i class="fa-brands fa-line"></i>
              </div>
              <div>
                <div class="text-xs text-slate-500">LINE Official / ID</div>
                <div class="text-sm font-bold text-green-600">manzx3 (คลิกเพื่อแอดไลน์)</div>
              </div>
            </a>

            <a href="https://www.facebook.com/Tel2tellcallcenter" target="_blank" class="flex items-center gap-4 p-3 rounded-xl bg-white border border-slate-200/80 hover:border-blue-600 transition group">
              <div class="w-11 h-11 rounded-xl bg-blue-50 text-blue-700 flex items-center justify-center font-bold text-xl group-hover:scale-105 transition">
                <i class="fa-brands fa-facebook"></i>
              </div>
              <div>
                <div class="text-xs text-slate-500">Facebook Page</div>
                <div class="text-sm font-bold text-blue-700">facebook.com/Tel2tellcallcenter</div>
              </div>
            </a>
          </div>

          <div class="p-6 bg-brand-navy rounded-2xl text-white space-y-2">
            <h4 class="font-bold text-sm text-brand-gold">บริษัท เทล ทู เทล จำกัด (Tel2tell Co., Ltd.)</h4>
            <p class="text-xs text-slate-300 font-sarabun leading-relaxed">
              ในเครือ SE BIZ Group ผู้ให้บริการ Outsource Contact Center, Fulfillment, Solar Energy และระบบสารสนเทศครบวงจร
            </p>
          </div>

        </div>

        <!-- Contact Form -->
        <div class="lg:col-span-7">
          <form id="contactForm" class="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm space-y-5" onsubmit="handleContactSubmit(event)">
            <h3 class="text-xl font-bold text-brand-navy pb-2 border-b border-slate-100">
              ส่งข้อความติดต่อ / ขอใบเสนอราคา
            </h3>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-slate-700 mb-1.5">ชื่อ-นามสกุล / บริษัท <span class="text-red-500">*</span></label>
                <input type="text" id="contactName" required placeholder="คุณสมชาย ใจดี" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-cyan">
              </div>

              <div>
                <label class="block text-xs font-semibold text-slate-700 mb-1.5">เบอร์โทรศัพท์ติดต่อ <span class="text-red-500">*</span></label>
                <input type="tel" id="contactPhone" required placeholder="08x-xxx-xxxx" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-cyan">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-slate-700 mb-1.5">อีเมล (E-mail)</label>
                <input type="email" id="contactEmail" placeholder="example@company.com" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-cyan">
              </div>

              <div>
                <label class="block text-xs font-semibold text-slate-700 mb-1.5">บริการที่สนใจ</label>
                <select id="contactService" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-cyan font-sarabun">
                  <option value="Inbound Call Center">Inbound Call Center (รับสายเข้า)</option>
                  <option value="Outbound Telesales">Outbound Telesales (โทรออกเชิงรุก)</option>
                  <option value="Sales Admin 24/7">Sales Admin 24/7 (แอดมินตอบแชท)</option>
                  <option value="VDO Production & Spot TV">VDO Production & สปอตทีวี</option>
                  <option value="Cloud IP PBX System">ระบบ Call Center Cloud IP PBX</option>
                  <option value="อื่นๆ">อื่นๆ / ปรึกษาภาพรวม</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1.5">รายละเอียดข้อความ <span class="text-red-500">*</span></label>
              <textarea id="contactMessage" required rows="4" placeholder="ระบุรายละเอียดงาน ขนาดทีม หรือข้อซักถามที่ต้องการ..." class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-sm focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-cyan font-sarabun"></textarea>
            </div>

            <!-- Simple Captcha -->
            <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span id="captchaQuestion" class="font-bold text-sm text-brand-navy">5 + 3 = ?</span>
              <input type="number" id="captchaAnswer" required placeholder="คำตอบ" class="w-24 bg-white border border-slate-300 rounded-lg px-3 py-1.5 text-sm text-center">
              <button type="button" onclick="generateCaptcha()" class="text-xs text-slate-500 hover:text-brand-cyan">
                <i class="fa-solid fa-rotate-right"></i> เปลี่ยนโจทย์
              </button>
            </div>

            <button type="submit" class="w-full py-3.5 bg-gradient-to-r from-brand-cyan to-blue-600 hover:from-sky-400 hover:to-blue-500 text-white font-bold rounded-xl shadow-lg shadow-sky-500/25 transition">
              ส่งข้อความติดต่อ
            </button>
          </form>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- FOOTER                                                         -->
  <!-- ============================================================== -->
  <footer class="bg-brand-dark text-slate-400 pt-16 pb-8 border-t border-slate-800 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-slate-800">
        
        <!-- Col 1: About & Logo -->
        <div class="lg:col-span-2 space-y-4">
          <div class="flex items-center gap-3">
            <img src="images/logo.png" alt="Tel2Tell" class="h-10 w-auto bg-white/90 p-1 rounded-lg">
            <span class="text-xl font-bold text-white tracking-wide font-prompt">TEL2TELL</span>
          </div>
          <p class="text-xs text-slate-400 font-sarabun leading-relaxed max-w-sm">
            บริษัท เทล ทู เทล จำกัด ผู้ให้บริการ Outsource Contact Center ครบวงจร ทั้งรับสายเข้าและโทรออก แนะนำการตลาดออฟไลน์และออนไลน์ มุ่งเน้นความปลอดภัยข้อมูลตามมาตรฐานสากล
          </p>
          <div class="text-xs space-y-1">
            <div><strong class="text-slate-300">Hotline:</strong> 089-040-4627</div>
            <div><strong class="text-slate-300">Email:</strong> nattapon@tel2tell.com</div>
            <div><strong class="text-slate-300">LINE ID:</strong> manzx3</div>
          </div>
        </div>

        <!-- Col 2: Services -->
        <div class="space-y-3">
          <h4 class="text-white font-bold text-sm tracking-wider">บริการของเรา</h4>
          <ul class="text-xs space-y-2">
            <li><a href="#services" class="hover:text-brand-accent transition">Inbound Call Center</a></li>
            <li><a href="outbound.html" class="hover:text-brand-accent transition">Outbound Telesales</a></li>
            <li><a href="sales-admin.html" class="hover:text-brand-accent transition">Sales Admin 24/7</a></li>
            <li><a href="vdo-production.html" class="hover:text-brand-accent transition">VDO Production & สปอตทีวี</a></li>
            <li><a href="#services" class="hover:text-brand-accent transition">ระบบ Call Center Cloud</a></li>
          </ul>
        </div>

        <!-- Col 3: Affiliates & SE BIZ -->
        <div class="space-y-3">
          <h4 class="text-white font-bold text-sm tracking-wider">เครือข่าย & พันธมิตร</h4>
          <ul class="text-xs space-y-2">
            <li><a href="https://www.facebook.com/Tel2tellcallcenter" target="_blank" class="hover:text-brand-accent transition">SE BIZ Group</a></li>
            <li><a href="https://www.fgfulfill.com/" target="_blank" class="hover:text-brand-accent transition">FG Logistics & Fulfillment</a></li>
            <li><a href="https://tel2solar.com/" target="_blank" class="hover:text-brand-accent transition">Tel2Solar พลังงานสะอาด</a></li>
            <li><a href="https://arapapashop.com/" target="_blank" class="hover:text-brand-accent transition">Arapapa Shop</a></li>
            <li><a href="https://www.dhipaya-training.com/" target="_blank" class="hover:text-brand-accent transition">Dhipaya Training Center</a></li>
          </ul>
        </div>

        <!-- Col 4: Newsletter & Live Stats -->
        <div class="space-y-4">
          <h4 class="text-white font-bold text-sm tracking-wider">รับข่าวสาร</h4>
          <p class="text-xs text-slate-400 font-sarabun">รับเทคนิคการขายและโปรโมชั่นพิเศษทางอีเมล</p>
          <form onsubmit="handleSubscribe(event)" class="space-y-2">
            <input type="email" required placeholder="กรอกอีเมลของคุณ" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:ring-1 focus:ring-brand-cyan">
            <button type="submit" class="w-full bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold text-xs py-2 rounded-lg transition">
              Subscribe
            </button>
          </form>

          <!-- Visitor Stats Widget -->
          <div class="pt-3 border-t border-slate-800 space-y-1 text-[11px]">
            <div class="flex justify-between">
              <span>ผู้เข้าชมทั้งหมด:</span>
              <span class="text-slate-200 font-mono font-bold">323,380+</span>
            </div>
            <div class="flex justify-between">
              <span>ผู้เข้าชมวันนี้:</span>
              <span class="text-green-400 font-mono font-bold">215</span>
            </div>
            <div class="flex justify-between">
              <span>ขณะนี้กำลังออนไลน์:</span>
              <span class="text-brand-accent font-mono font-bold flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span> 42 คน
              </span>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs">
        <div>
          &copy; 2017-2026 <strong>Tel2tellcallcenter.com</strong> All Rights Reserved.
        </div>
        <div class="flex items-center gap-6">
          <a href="#" onclick="openPolicyModal('privacy')" class="hover:text-white transition">นโยบายความเป็นส่วนตัว (Privacy Policy)</a>
          <a href="#" onclick="openPolicyModal('cookies')" class="hover:text-white transition">นโยบายคุกกี้ (Cookies Policy)</a>
          <a href="jobs.html" class="text-brand-gold hover:underline">ร่วมงานกับเรา</a>
        </div>
      </div>

    </div>
  </footer>

  <!-- ============================================================== -->
  <!-- FLOATING ACTION BUTTONS (STICKY)                               -->
  <!-- ============================================================== -->
  <div class="fixed bottom-6 right-6 z-40 flex flex-col items-end gap-3">
    <!-- Quick Call Button -->
    <a href="tel:0890404627" class="w-12 h-12 bg-blue-600 hover:bg-blue-500 text-white rounded-full flex items-center justify-center shadow-2xl shadow-blue-600/40 hover:scale-110 transition group relative" title="โทรด่วน 089-040-4627">
      <i class="fa-solid fa-phone text-lg"></i>
      <span class="absolute right-14 bg-slate-900 text-white text-xs px-2.5 py-1 rounded-lg shadow whitespace-nowrap opacity-0 group-hover:opacity-100 transition pointer-events-none">
        โทร: 089-040-4627
      </span>
    </a>

    <!-- LINE Button -->
    <a href="http://line.me/ti/p/~manzx3" target="_blank" class="w-12 h-12 bg-brand-line hover:bg-green-500 text-white rounded-full flex items-center justify-center shadow-2xl shadow-green-600/40 hover:scale-110 transition group relative" title="คุยผ่าน LINE: manzx3">
      <i class="fa-brands fa-line text-2xl"></i>
      <span class="absolute right-14 bg-slate-900 text-white text-xs px-2.5 py-1 rounded-lg shadow whitespace-nowrap opacity-0 group-hover:opacity-100 transition pointer-events-none">
        LINE: manzx3
      </span>
    </a>
  </div>

  <!-- ============================================================== -->
  <!-- MODAL: ARTICLE READER                                          -->
  <!-- ============================================================== -->
  <div id="articleModal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-3xl w-full max-h-[90vh] flex flex-col overflow-hidden shadow-2xl animate-in fade-in zoom-in-95 duration-200">
      
      <!-- Modal Header -->
      <div class="p-5 border-b border-slate-200 flex items-center justify-between bg-slate-50">
        <span id="modalArticleCategory" class="px-2.5 py-1 text-xs font-bold bg-brand-cyan/10 text-brand-cyan rounded-full">
          หมวดหมู่
        </span>
        <button onclick="closeArticleModal()" class="w-8 h-8 rounded-full bg-slate-200 hover:bg-slate-300 text-slate-700 flex items-center justify-center transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="p-6 sm:p-8 overflow-y-auto space-y-6">
        <h2 id="modalArticleTitle" class="text-2xl font-bold text-brand-navy leading-snug">
          ชื่อบทความ
        </h2>
        <div id="modalArticleImageContainer" class="rounded-xl overflow-hidden max-h-72 bg-slate-100">
          <img id="modalArticleImage" src="" alt="" class="w-full h-full object-cover">
        </div>
        <div id="modalArticleContent" class="text-slate-700 text-sm sm:text-base font-sarabun leading-relaxed space-y-4 whitespace-pre-line">
          เนื้อหาบทความ...
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-slate-200 bg-slate-50 flex items-center justify-between">
        <span class="text-xs text-slate-400">Tel2Tell Knowledge Base</span>
        <div class="flex items-center gap-2">
          <a href="#contact" onclick="closeArticleModal()" class="px-4 py-2 bg-brand-cyan text-white text-xs font-bold rounded-lg hover:bg-sky-500 transition">
            ปรึกษาผู้เชี่ยวชาญ
          </a>
          <button onclick="closeArticleModal()" class="px-4 py-2 bg-slate-200 text-slate-700 text-xs font-semibold rounded-lg hover:bg-slate-300 transition">
            ปิดหน้าต่าง
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- ============================================================== -->
  <!-- MODAL: JOB APPLICATION FORM                                    -->
  <!-- ============================================================== -->
  <div id="jobModal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-lg w-full max-h-[90vh] overflow-y-auto shadow-2xl p-6 sm:p-8 space-y-5 animate-in fade-in duration-200">
      <div class="flex items-center justify-between border-b border-slate-100 pb-3">
        <div>
          <h3 class="text-lg font-bold text-brand-navy">แบบฟอร์มสมัครงาน</h3>
          <p id="jobModalPosition" class="text-xs font-semibold text-brand-cyan">ตำแหน่ง: Telesales</p>
        </div>
        <button onclick="closeJobModal()" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <form onsubmit="handleJobSubmit(event)" class="space-y-4">
        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">ชื่อ-นามสกุล <span class="text-red-500">*</span></label>
          <input type="text" required placeholder="นาย/นางสาว สมหวัง มุ่งมั่น" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">เบอร์โทรศัพท์ <span class="text-red-500">*</span></label>
            <input type="tel" required placeholder="08x-xxx-xxxx" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">อายุ (ปี) <span class="text-red-500">*</span></label>
            <input type="number" min="18" max="50" required placeholder="เช่น 25" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan">
          </div>
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">วุฒิการศึกษาสูงสุด <span class="text-red-500">*</span></label>
          <select required class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan font-sarabun">
            <option value="ม.3 / ม.6">มัธยมศึกษาตอนต้น / ตอนปลาย (ม.3 / ม.6)</option>
            <option value="ปวช. / ปวส.">ปวช. / ปวส.</option>
            <option value="ปริญญาตรี">ปริญญาตรี</option>
            <option value="อื่นๆ">อื่นๆ</option>
          </select>
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">ประสบการณ์ทำงานที่เกี่ยวข้อง</label>
          <textarea rows="3" placeholder="ระบุประสบการณ์ Telesales, Callcenter, แอดมิน หรืออื่นๆ (ถ้ามี)" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-cyan font-sarabun"></textarea>
        </div>

        <div class="text-[11px] text-slate-500 font-sarabun">
          <i class="fa-solid fa-circle-info text-brand-cyan mr-1"></i> เจ้าหน้าที่ฝ่ายบุคคลจะติดต่อกลับเพื่อนัดสัมภาษณ์งานภายใน 24 ชม.
        </div>

        <button type="submit" class="w-full py-3 bg-brand-cyan hover:bg-sky-400 text-brand-dark font-bold text-sm rounded-xl transition">
          ส่งใบสมัครทันที
        </button>
      </form>
    </div>
  </div>

  <!-- Load Article Data & Interactive Scripts -->
  <script src="articles-data.js"></script>
  <script>
    // Mobile Drawer Toggle
    const mobileBtn = document.getElementById('mobileMenuBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');
    mobileBtn.addEventListener('click', () => {
      mobileDrawer.classList.toggle('hidden');
    });

    // Captcha Logic
    let num1 = 5, num2 = 3;
    function generateCaptcha() {
      num1 = Math.floor(Math.random() * 9) + 1;
      num2 = Math.floor(Math.random() * 9) + 1;
      document.getElementById('captchaQuestion').textContent = `${num1} + ${num2} = ?`;
      document.getElementById('captchaAnswer').value = '';
    }

    function handleContactSubmit(e) {
      e.preventDefault();
      const ans = parseInt(document.getElementById('captchaAnswer').value, 10);
      if (ans !== (num1 + num2)) {
        alert('กรุณากรอกคำตอบคำนวณ Captcha ให้ถูกต้อง');
        return;
      }
      const name = document.getElementById('contactName').value;
      alert(`ขอบคุณครับ คุณ ${name}\n\nข้อความของคุณถูกส่งเรียบร้อยแล้ว ทีมงาน Tel2Tell จะรีบติดต่อกลับโดยเร็วที่สุดครับ!`);
      document.getElementById('contactForm').reset();
      generateCaptcha();
    }

    function handleSubscribe(e) {
      e.preventDefault();
      alert('ได้รับข้อมูลของคุณเรียบร้อยแล้ว ขอบคุณสำหรับการติดตามข่าวสารจาก Tel2Tell Call Center');
      e.target.reset();
    }

    // Dynamic Article Rendering & Filtering
    let currentCategory = 'all';
    let searchQuery = '';

    function renderArticles() {
      const grid = document.getElementById('articlesGrid');
      if (!window.TEL2TELL_ARTICLES) return;

      let filtered = window.TEL2TELL_ARTICLES;

      if (currentCategory !== 'all') {
        filtered = filtered.filter(a => a.category === currentCategory);
      }

      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        filtered = filtered.filter(a => a.title.toLowerCase().includes(q) || a.excerpt.toLowerCase().includes(q));
      }

      // Limit to 6 initially unless searching or viewing all
      const displayList = filtered.slice(0, 6);

      grid.innerHTML = displayList.map(a => `
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden card-hover flex flex-col justify-between shadow-sm">
          <div class="h-48 overflow-hidden bg-slate-100 relative">
            <img src="${a.image}" alt="${a.title}" class="w-full h-full object-cover transform hover:scale-105 transition duration-500" onerror="this.src='images/articles/art_1.png'">
            <span class="absolute top-3 left-3 bg-brand-navy/90 backdrop-blur text-white text-[11px] font-semibold px-2.5 py-0.5 rounded-full">
              ${a.category}
            </span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h3 class="font-bold text-brand-navy text-base leading-snug line-clamp-2 hover:text-brand-cyan transition cursor-pointer" onclick="openArticleModal('${a.id}')">
                ${a.title}
              </h3>
              <p class="text-xs text-slate-600 font-sarabun mt-2 line-clamp-3 leading-relaxed">
                ${a.excerpt}
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
              <span class="text-[11px] text-slate-400">Tel2Tell Insights</span>
              <button onclick="openArticleModal('${a.id}')" class="text-xs font-bold text-brand-cyan hover:text-sky-700 flex items-center gap-1">
                อ่านต่อ <i class="fa-solid fa-arrow-right text-[10px]"></i>
              </button>
            </div>
          </div>
        </div>
      `).join('');
    }

    // Category Filter Buttons
    document.querySelectorAll('.cat-filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.cat-filter-btn').forEach(b => {
          b.classList.remove('bg-brand-navy', 'text-white');
          b.classList.add('bg-white', 'text-slate-700');
        });
        btn.classList.add('bg-brand-navy', 'text-white');
        btn.classList.remove('bg-white', 'text-slate-700');
        currentCategory = btn.getAttribute('data-cat');
        renderArticles();
      });
    });

    // Search Input
    document.getElementById('articleSearchInput').addEventListener('input', (e) => {
      searchQuery = e.target.value;
      renderArticles();
    });

    // View All Articles Button
    document.getElementById('viewAllArticlesBtn').addEventListener('click', () => {
      currentCategory = 'all';
      searchQuery = '';
      const grid = document.getElementById('articlesGrid');
      grid.innerHTML = window.TEL2TELL_ARTICLES.map(a => `
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden card-hover flex flex-col justify-between shadow-sm">
          <div class="h-44 overflow-hidden bg-slate-100 relative">
            <img src="${a.image}" alt="${a.title}" class="w-full h-full object-cover transform hover:scale-105 transition duration-500" onerror="this.src='images/articles/art_1.png'">
            <span class="absolute top-3 left-3 bg-brand-navy/90 backdrop-blur text-white text-[11px] font-semibold px-2.5 py-0.5 rounded-full">
              ${a.category}
            </span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-3">
            <div>
              <h3 class="font-bold text-brand-navy text-sm leading-snug line-clamp-2 hover:text-brand-cyan transition cursor-pointer" onclick="openArticleModal('${a.id}')">
                ${a.title}
              </h3>
              <p class="text-xs text-slate-600 font-sarabun mt-1 line-clamp-2 leading-relaxed">
                ${a.excerpt}
              </p>
            </div>
            <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
              <span class="text-[10px] text-slate-400">Tel2Tell Insights</span>
              <button onclick="openArticleModal('${a.id}')" class="text-xs font-bold text-brand-cyan hover:text-sky-700">
                อ่านต่อ &rarr;
              </button>
            </div>
          </div>
        </div>
      `).join('');
      document.getElementById('viewAllArticlesBtn').style.display = 'none';
    });

    // Article Modal Logic
    function openArticleModal(id) {
      const art = window.TEL2TELL_ARTICLES.find(a => a.id === id);
      if (!art) return;

      document.getElementById('modalArticleTitle').textContent = art.title;
      document.getElementById('modalArticleCategory').textContent = art.category;
      document.getElementById('modalArticleImage').src = art.image;
      document.getElementById('modalArticleContent').textContent = art.content || art.excerpt;

      document.getElementById('articleModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeArticleModal() {
      document.getElementById('articleModal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }

    // Job Modal Logic
    function openJobModal(pos) {
      document.getElementById('jobModalPosition').textContent = `ตำแหน่ง: ${pos}`;
      document.getElementById('jobModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeJobModal() {
      document.getElementById('jobModal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }

    function handleJobSubmit(e) {
      e.preventDefault();
      alert('ส่งข้อมูลการสมัครงานเรียบร้อยแล้ว! ฝ่ายบุคคล Tel2Tell จะติดต่อกลับเพื่อนัดสัมภาษณ์โดยเร็วที่สุดครับ');
      closeJobModal();
    }

    function openPolicyModal(type) {
      if (type === 'privacy') {
        alert('นโยบายความเป็นส่วนตัว (PDPA): บริษัท เทล ทู เทล จำกัด ให้ความสำคัญสูงสุดในการรักษาความปลอดภัยของข้อมูลส่วนบุคคลของลูกค้าและผู้ใช้บริการ ตามกฎเกณฑ์พระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ข้อมูลของท่านจะไม่ถูกเปิดเผยแก่บุคคลภายนอกโดยไม่ได้รับความยินยอม');
      } else {
        alert('นโยบายคุกกี้ (Cookies Policy): เว็บไซต์นี้มีการใช้งานคุกกี้เพื่อเพิ่มประสิทธิภาพและมอบประสบการณ์ที่ดีที่สุดในการใช้งานของท่าน');
      }
    }

    // Initial run
    generateCaptcha();
    renderArticles();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html created successfully!")
