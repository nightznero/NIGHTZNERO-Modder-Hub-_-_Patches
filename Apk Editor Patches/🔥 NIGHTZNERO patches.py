Patch to Remove analytics, telemetry and metrics and so on.

[AUTHOR]
NIGHTZNERO

Target:
smali*/*.smali Files & .xml File

Regex:
true

━━━━━━━━━━━━━━━━━━━━━━
          Target: ".xml" file patches | Regex: true
━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━
Analytics-Telematry-Metrics Remover
Search .xml:
		<service android:exported="(.+)" android:name="com.google.firebase(.+)">\n			<intent-filter android:priority="(.+)">\n				<action android:name="com.google.firebase(.+)" />\n			</intent-filter>\n		</service>
Search .xml:
		<receiver android:exported="(.+)" android:name="com.google.firebase(.+)" />
━━━━━━━━━━━━━━━━━━━━━━
Disabling Google Play Billing Services
Search .xml:
<uses-permission android:name="com.android.vending.BILLING" />
━━━━━━━━━━━━━━━━━━━━━━





━━━━━━━━━━━━━━━━━━━━━━
          Target: "res/layout*/*.xml" file patches | Regex: true
━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━
Google banner ads
Search:
(<\S*[^<]*)(android:id=\"@id/(?:[Aa][Dd][Ss]|[Bb][Aa][Nn][Nn][Ee][Rr]|[Aa][Dd][Vv][Ii][Ee][Ww]|[Aa][Dd][Vv][Ii][Ee][Ww]Layout)\") (.+)

Replace:
${GROUP1}${GROUP2} android:visibility="gone" ${GROUP3}



Search:
<com.google.android.gms.ads.AdView (.+)

Replace:
<com.google.android.gms.ads.AdView android:visibility="gone" ${GROUP1}
━━━━━━━━━━━━━━━━━━━━━━





━━━━━━━━━━━━━━━━━━━━━━
          Target: "smali*/*.smali" files patches | Regex: true
━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━
Analytics-Telematry-Metrics Remover
Search:
\"https://graph\.%s\"|\".*branch\.io\"|\".*api\.branch\.io\"|\".*api2\.branch\.io\"|\".*sentry\.io.*\"|\".*crashlytics\.com.*\"|\".*wzrkt\.com*\"|\".*appboy\.com*\"|\".*.appsflyer\.com/.*\"|\".*.applovin\.com/.*\"|\".*.bugsnag\.com/.*\"|\".*google-analytics\.com.*\"|\"ssl\.google-analytics\.com.*\"|\".*.google-analytics\.com.*\"|\".*measurement\.com.*\"|\".*data.flurry\.com.*\"|\".*googletagmanager\.com.*\"|\".*hockeyapp\.net.*\"|\".*scorecardresearch\.com.*\"|\".*YandexMetricaNativeModule*\"|\".*amplitude\.com.*\"|\".*azure\.com.*\"|\".*firebaseapp\.com.*\"|\".*startappservice\.com.*\"|\".*startappexchange\.com.*\"|\".*smaato\.com.*\"|\".*api\.crittercism\.com\"|\".*appmetrica\.yandex\.ru\"|\".*app\.adjust\.com\"|\".*app\.adjust\.net\.in\"|\".*app\.adjust\.world\"|\".*app\.adjust\.io\"|\".*cloudfront\.net.*\"|\".*amazonaws\.com.*\"|\".*akamaitechnologies\.com.*\"|\"microsoft\.applications\.telemetry.*\"|\"skype\.telemetry\.com.*\"|\"skype\.android\.analytics\.com.*\"|\"skype\.android\.crash\.com.*\"|\".*chartboost\.com.*\"|\".*my\.target\.com\"|\".*umeng\.com.*\"|\".*umengcloud\.com.*\"|\".*lsdsl\.ml.*\"|\".*doubleclick\.net.*\"|\".*googleadservices\.com.*\"|\".*pagead/ads.*\"|\".*googleads.*\"|\".*ad\.doubleclick\.net.*\"

Replace:
"="
━━━━━━━━━━━━━━━━━━━━━━
Low/Medium/High-level Patch for Disabling Ads from Android Apps and Games

StringSearch:
"(http.*|//.*)(61\.145\.124\.238|/2mdn\.net|-ads\.|\.5rocks\.io|\.ad\.|\.adadapted|\.admitad\.|\.admost\.|\.ads\.|\.aerserv\.|\.airpush\.|\.batmobil\.|\.chartboost\.|\.cloudmobi\.|\.conviva\.|\.dov-e\.com|\.fyber\.|\.mng-ads\|\.mydas\.|\.predic\.|\.talkingdata\.|\.tapdaq\.|\.tele\.fm|\.unity3d\.|\.unity\.|\.wapstart\.|\.xdrig\.|\.zapr\.|\/ad\.|\/ads|a4\.tl|accengage|ad4push|ad4screen|ad-mail|ad\..*_logging|ad\.api\.kaffnet\.|ad\.cauly\.co\.|adbuddiz|adc3-launch|adcolony|adfurikun|adincube|adinformation|adkmob|admax\.|admixer|admob|admost|ads\.mdotm\.|adsafeprotected|adservice|adsmogo|adsrvr|adswizz|adtag|adtech\.de|advert|adwhirl|adz\.wattpad\.|alimama\.|alta\.eqmob\.|amazon-.*ads|amazon\..*ads|amobee|analytics|anvato|appboy|appbrain|applovin|applvn|appmetrica|appnext|appodeal|appsdt|appsflyer|apsalar|avocarrot|axonix|banners-slb\.mobile\.yandex\.net|banners\.mobile\.yandex\.net|brightcove\.|burstly|cauly|cloudfront|cmcm\.|com\.google\.android\.gms\.ads\.identifier\.service\.START|comscore|contextual\.media\.net|crashlytics|crispwireless|criteo\.|dmtry\.|doubleclick|duapps|dummy|flurry|fwmrm|gad|getads|gimbal|glispa|google\.com\/dfp|googleAds|googleads|googleapis\..*\.ad-.*|googlesyndication|googletagmanager|greystripe|gstatic|heyzap|hyprmx|iasds01|inmobi|inneractive|instreamatic|integralads|jumptag|jwpcdn|jwpltx|jwpsrv|kochava|localytics|madnet|mapbox|mc\.yandex\.ru|media\.net|metrics\.|millennialmedia|mixpanel|mng-ads\.com|moat\.|moatads|mobclix|mobfox|mobpowertech|moodpresence|mopub|native_ads|nativex\.|nexage\.|ooyala|openx\.|pagead|pingstart|prebid|presage\.io|pubmatic|pubnative|rayjump|saspreview|scorecardresearch|smaato|smartadserver|sponsorpay|startappservice|startup\.mobile\.yandex\.net|statistics\.videofarm\.daum\.net|supersonicads|taboola|tapas|tapjoy|tapylitics|target\.my\.com|teads\.|umeng|unityads|vungle|zucks).*"

Replace:
"127.0.0.1"

-------------------------

VoidSearch:
(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>(.*(load|show).*)\(.*\)V)
VoidSearch:
(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>((.*(Banner|initAd|Interstitial|load|Native|onAd|Rewarded|show|(fetch|refresh|render|request|video)Ad).*))\(.*\)V)
VoidSearch:
(invoke(?!.*(close|Deactiv|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop|Throw)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>(request.*|(.*(activat|Banner|build|Event|exec|header|html|initAd|initi|JavaScript|Interstitial|load|log|MetaData|metri|Native|onAd|propert|report|response|Rewarded|show|trac|url|(fetch|refresh|render|video)Ad).*)|.*Request)\(.*\)V)

Replace:
nop

-------------------------

BooleanSearch:
(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>(.*(load|show).*)\(.*\)Z\n\n\s{4})move-result\s([pv]\d+)
BooleanSearch:
(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>((.*(Banner|initAd|Interstitial|load|Native|(can|get|has|is|was)Ad|Rewarded|show|(fetch|refresh|render|request|video)Ad).*))\(.*\)Z\n\n\s{4})move-result\s([pv]\d+)
BooleanSearch:
(invoke(?!.*(close|Deactiv|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop|Throw)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>(request.*|(.*(activat|Banner|build|Event|exec|header|html|initAd|initi|JavaScript|Interstitial|load|log|MetaData|metri|Native|(can|get|is|has|was)Ad|propert|report|response|Rewarded|show|trac|url|(fetch|refresh|render|video)Ad).*)|.*Request)\(.*\)Z\n\n\s{4})move-result\s([pv]\d+)

Replace:
const/4 $6, 0x0
Replace:
const/4 $9, 0x0
Replace:
const/4 $9, 0x0
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v5 (carefully)
Search:
"(http.*|//.*)(61.145.124.238|-ads.|.ad.|.ads.|.analytics.localytics.com|.mobfox.com|.mp.mydas.mobi|.plus1.wapstart.ru|.scorecardresearch.com|.startappservice.com|/ad.|/ads|ad-mail|ad.*_logging|ad.api.kaffnet.com|adc3-launch|adcolony|adinformation|adkmob|admax|admob|admost|adsafeprotected|adservice|adtag|advert|adwhirl|adz.wattpad.com|alta.eqmob.com|amazon-*ads|amazon.*ads|amobee|analytics|applovin|applvn|appnext|appodeal|appsdt|appsflyer|burstly|cauly|cloudfront|com.google.android.gms.ads.identifier.service.START|crashlytics|crispwireless|doubleclick|dsp.batmobil.net|duapps|dummy|flurry|gad|getads|google.com/dfp|googleAds|googleads|googleapis.*.ad-*|googlesyndication|googletagmanager|greystripe|gstatic|inmobi|inneractive|jumptag|live.chartboost.com|madnet|millennialmedia|moatads|mopub|native_ads|pagead|pubnative|smaato|supersonicads|tapas|tapjoy|unityads|vungle|zucks).*"

Replace:
"="
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v6
Search:
(invoke.*gms.*\>(loadUrl|loadDataWithBaseURL|requestInterstitialAd|showInterstitial|showVideo|showAd|loadData|onAdClicked|onAdLoaded|isLoading|loadAds|AdLoader|AdRequest|AdListener|AdView).*V)

Replace:
#$1
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v7
Search:
(invoke.*loadAd\(.*\)[VZ])

Replace:
#$1
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v3 *Reward*
Search:
invoke-.*\{.*\}, L.*;->(loadAd|requestNativeAd|showInterstitial|fetchad|fetchads|onadloaded|requestInterstitialAd|showAd|loadAds|AdRequest|requestBannerAd|loadNextAd|createInterstitialAd|setNativeAd|loadBannerAd|loadNativeAd|loadRewardedAd|loadRewardedInterstitialAd|loadAds|loadAdViewAd|showInterstitialAd|shownativead|showbannerad|showvideoad|onAdFailedToLoad)\(.*\)V

Replace:
nop
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v10 *Reward* (safer v12 patch)
Search:
(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>((.*(Banner|initAd|Interstitial|load|Native|onAd|Rewarded|show|(fetch|refresh|render|request|video)Ad).*))\(.*\)V)

Replace:
nop
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v12 *Reward*
Search:
(invoke(?!.*(close|Deactiv|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop|Throw)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/.*>(request.*|(.*(activat|Banner|build|Event|exec|header|html|initAd|initi|JavaScript|Interstitial|load|log|MetaData|metri|Native|onAd|propert|report|response|Rewarded|show|trac|url|(fetch|refresh|render|video)Ad).*)|.*Request)\(.*\)V)

Replace:
nop
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v1 *Reward*
Search:
(\.method.*(loadAd|requestNativeAd|showInterstitial|fetchad|fetchads|onadloaded|requestInterstitialAd|showAd|loadAds|AdRequest|requestBannerAd|loadNextAd|createInterstitialAd|setNativeAd|loadBannerAd|loadNativeAd|loadRewardedAd|loadRewardedInterstitialAd|loadAds|loadAdViewAd|showInterstitialAd|shownativead|showbannerad|showvideoad|onAdFailedToLoad)\(.*\)V     \.registers \d+)[\s\S]*?\.end method

Replace:
#
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v4
Search:
ca-app-pub-\d{16}/\d{10}

Replace:
ca-app-pub-0000000000000000/0000000000
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v9
Search:
(\.method\s(public|private|static)\s\b(?!\babstract|native\b)(.*)?loadAd\(.*\)V)

Replace:
$1

return-void
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v8
Search:
(\.method\s(public|private|static)\s\b(?!\babstract|native\b)(.*)?loadAd\(.*\)Z)

Replace:
$1

    const/4 v0, 0x0

    return v0
━━━━━━━━━━━━━━━━━━━━━━
Remove Ads v2 (carefully!)
Search:
invoke-*.* \{*.*\}, Lcom*.*;->requestInterstitialAd\(*.*\)V|invoke-*.* \{*.*\}, Lcom*.*;->loadAds\(*.*\)V|invoke-*.* \{*.*\}, Lcom*.*;->loadAd\(*.*\)V|invoke-*.* \{*.*\}, Lcom*.*;->requestBannerAd\(*.*\)V|invoke-*.*\s\{[v|p]\d\},\sLcom/facebook*.*\;\-\>show\(*.*\)V|invoke-*.*\s\{[v|p]\d\},\sLcom/google*.*\;\-\>show\(*.*\)V

Replace:
nop
━━━━━━━━━━━━━━━━━━━━━━
Remove Google banner ads
Search:
const/(\d+) ([pv]\d+), 0x(\d+)\n\n    invoke-virtual \{([pv]\d+), ([pv]\d+)\}, Lcom/google/android/gms/ads/AdView;->setVisibility\(I\)V

Replace:
    const ${GROUP2}, 0x8

    invoke-virtual {${GROUP4}, ${GROUP2}}, Lcom/google/android/gms/ads/AdView;->setVisibility(I)V
━━━━━━━━━━━━━━━━━━━━━━
Firebase Analytics Remover

Search:
"com.google.analytics
Replace:
"disabled_com.google.analytics

Search:
"com.google.android.gms.analytics
Replace:
"disabled_com.google.android.gms.analytics

Search:
"com.google.firebase.analytics
Replace:
"disabled_com.google.firebase.analytics

Search:
"com.google.firebase.firebase_analytics
Replace:
"disabled_com.google.firebase.firebase_analytics
━━━━━━━━━━━━━━━━━━━━━━
Disabling Google Play Billing Services
Search:
"com.android.vending.billing

Replace:
"disabled_com.android.vending.billing
━━━━━━━━━━━━━━━━━━━━━━
Disabling Google Play Services
Search:
.method public static(.+)\(Landroid/content/Context;\)I\n.*registers .+[\s\S]*?Google Play services missing.+[\s\S]*?end method

Replace:
.method public static${GROUP1}(Landroid/content/Context;)I
    .registers 1
    const/4 v0, 0x0
    return v0
.end method



Search:
invoke-virtual \{([pv]\d+), ([pv]\d+)\}, Ljava/security/Signature;->verify\(\[B\)Z\n\n    move-result ([pv]\d+)

Replace:
invoke-virtual {${GROUP1}, ${GROUP2}}, Ljava/security/Signature;->verify([B)Z

    const/4 ${GROUP3}, 0x1
━━━━━━━━━━━━━━━━━━━━━━
Disabling Google Play Games
Search:
const-string ([pv]\d+), "com.google.android.gms.auth.NO_IMPL"\s*(.*)\s*invoke-virtual \{([pv]\d+), ([pv]\d+)\}, Ljava/lang/String;->equals(.+)\s*(.*)\s*move-result ([pv]\d+)
Replace:
const/4 ${GROUP1}, 0x1



Search:
com.google.android.gms.auth.api.signin.service.START
Replace:
com.google.android.gms.auth.api.signin.service.STOP
━━━━━━━━━━━━━━━━━━━━━━
AOSP
Search:
isGooglePlayServicesAvailable

Replace:
GooglePlayServicesErrorDialog
━━━━━━━━━━━━━━━━━━━━━━
Disabling VPN Detection
Search:
invoke-virtual .*, Landroid/net/NetworkInfo.*isConnectedOrConnecting\(\)Z

    move-result (.*)

Replace:
const $1, 0x0
━━━━━━━━━━━━━━━━━━━━━━
❰ Manufacturer ❱
The manufacturer of the product/hardware.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->MANUFACTURER:Ljava/lang/String;
Replace:
const-string $1, "Xiaomi"
━━━━━━━━━━━━━━━━━━━
❰ Brand ❱
The consumer-visible brand with which the product/hardware will be associated, if any.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->BRAND:Ljava/lang/String;
Replace:
const-string $1, "Xiaomi"
━━━━━━━━━━━━━━━━━━━
❰ Model ❱
The end-user-visible name for the end product.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->MODEL:Ljava/lang/String;
Replace:
const-string $1, "Redmi K20 Pro"
━━━━━━━━━━━━━━━━━━━
❰ Product ❱
The name of the overall product.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->PRODUCT:Ljava/lang/String;
Replace:
const-string $1, "raphael"
━━━━━━━━━━━━━━━━━━━
❰ Device ❱
The name of the industrial design.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->DEVICE:Ljava/lang/String;
Replace:
const-string $1, "raphael"
━━━━━━━━━━━━━━━━━━━
❰ Board ❱
The name of the underlying board, like "goldfish".

Search:
sget-object ([pv]\d+), Landroid/os/Build;->BOARD:Ljava/lang/String;
Replace:
const-string $1, "raphael"
━━━━━━━━━━━━━━━━━━━
❰ Radio ❱
The radio firmware version number.

Search:
invoke-static \{\}, Landroid/os/Build;->getRadioVersion\(\)Ljava/lang/String;\n\n    move-result-object ([pv]\d+)

Or
Search:
sget-object ([pv]\d+), Landroid/os/Build;->RADIO:Ljava/lang/String;

Replace:
const-string $1, "Unknown"
━━━━━━━━━━━━━━━━━━━
❰ Hardware ❱
The name of the hardware (from the kernel command line or /proc).

Search:
sget-object ([pv]\d+), Landroid/os/Build;->HARDWARE:Ljava/lang/String;
Replace:
const-string $1, "qcom"
━━━━━━━━━━━━━━━━━━━
❰ Bootloader ❱
The system bootloader version number.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->BOOTLOADER:Ljava/lang/String;
Replace:
const-string $1, "Unknown"
━━━━━━━━━━━━━━━━━━━
❰ Fingerprint ❱
A string that uniquely identifies this build. Do not attempt to parse this value.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->FINGERPRINT:Ljava/lang/String;
Replace:
const-string $1, "Xiaomi/raphael/raphael:11/RKQ1.200826.002/V12.5.4.0.RFKCNXM:user/release-keys"
━━━━━━━━━━━━━━━━━━━
❰ ID ❱
Either a changelist number, or a label like "M4-rc20".

Search:
sget-object ([pv]\d+), Landroid/os/Build;->ID:Ljava/lang/String;
Replace:
const-string $1, "RKQ1.200826.002"
━━━━━━━━━━━━━━━━━━━
❰ Serial ❱
A hardware serial number, if available. Alphanumeric only, case-insensitive. This field is always set to Build#UNKNOWN.

Search:
sget-object ([pv]\d+), Landroid/os/Build;->SERIAL:Ljava/lang/String;
Replace:
const-string $1, "Unknown"
━━━━━━━━━━━━━━━━━━━━━━
Fake IMEI
Search #1:
invoke-virtual \{([pv]\d+)\}, Landroid/telephony/TelephonyManager;->getDeviceId\(\)Ljava/lang/String;\n\n    move-result-object ([pv]\d+)

Replace #1:
    const-string ${GROUP2}, "please_input_IMEI"

-------------------------

Search #2:
invoke-virtual \{([pv]\d+)\}, Landroid/telephony/TelephonyManager;->getDeviceId\(\)Ljava/lang/String;\n    :try_end_(.+)\n    \.catch (.+); \{:try_start_(.+) .. :try_end_(.+)\} :catch_(.+)\n\n    move-result-object ([pv]\d+)

Replace #2:
invoke-virtual {${GROUP1}}, Landroid/telephony/TelephonyManager;->getDeviceId()Ljava/lang/String;
    :try_end_${GROUP2}
    .catch ${GROUP3}; {:try_start_${GROUP4} .. :try_end_${GROUP5}} :catch_${GROUP6}

    const-string ${GROUP7}, "input_IMEI"
━━━━━━━━━━━━━━━━━━━━━━
Fake IP
Search:
iget-object ([pv]\d+), ([pv]\d+), L(\S+);->ip:Ljava/lang/String;

Replace:
const-string ${GROUP1}, "255.255.255.255"
━━━━━━━━━━━━━━━━━━━━━━
Fake GPS
Search #1:
invoke-virtual \{([pv]\d+)\}, Landroid/location/Location;->getLatitude\(\)D\n\n    move-result-wide ([pv]\d+)

Replace #1:
const-wide ${GROUP2}, 0x404a01a6f3f52fbcL    # 52.012907499999955

-------------------------

Search #2:
invoke-virtual \{([pv]\d+)\}, Landroid/location/Location;->getLongitude\(\)D\n\n    move-result-wide ([pv]\d+)

Replace #2:
const-wide ${GROUP2}, 0x405c5e47be76c8b2L    # 113.47312890624997
━━━━━━━━━━━━━━━━━━━━━━
Screenshot restrictions disabling
Search:
invoke-virtual (\{.*\}), Landroid/view/Window;->addFlags\(I\)V
invoke-virtual (\{.*\}), Landroid/view/Window;->setFlags\(II\)V

Replace:
#$1
━━━━━━━━━━━━━━━━━━━━━━
Unlocking Premium (dependence of aboved "move-result" is V or P)
const/4 v0, 0x1
const/4 p0, 0x1
codes for premium
Search:
\b(
  vipuser|ispro|isprouser|ispremium|ispremiumuser|
  alreadyvip|ispurchased|unlocked|adremoved|gopremium|
  removed_ads|is_subscribed|subscribe_pro|ispurchase|
  purchase|ispremium|getpremium|mispremium|"pro"ispro|
  subscribe|vip|isuservip|vipaccess|proaccess|
  premiumaccess|subscribeduser|prosubscription|
  premiumsubscription|purchasedsubscription|vipsubscription|
  is_vip_subscribed|is_pro_subscribed|is_premium_subscribed|
  pro_member|premium_member|subscribed_member|pro_membership|
  premium_membership|purchased_membership|vip_membership|
  is_vip_member|is_pro_member|is_premium_member|
  vip_status|pro_status|premium_status|
  vip_plan|pro_plan|premium_plan|
  vip_upgrade|pro_upgrade|premium_upgrade|
  vip_feature|pro_feature|premium_feature|
  vip_content|pro_content|premium_content|
  accountType | isProVersion | "PRO" | isAppPro | PURCHASE_PRO |
  feature | feature.trial | feature.pro | subscription |
  isAppPro: " | subscription_type | isOfferWallAvailable |
  You\'ve already subscribed ! | EMPTY license | inc_gp_sub_001 |
  ismember | "LicenseInfo" | SUPPRESS_SUB_ALERTS |
  plan_feature | key_event_vip | isPro\(\)Z |
  licenceDuration" | key_billing_vip |
  PRO_VERSION | is_user_premium |
  licenseUtils | hasAdware\(\)Z |
  isProUser" | paid_premium_upgrade" |
  IS_HAS_SUBSCRIPTION" | premium_mode_enabled |
  isPro\(\)Z | pro_version |
  LicenseStatus | isVipPurchased |
  donate_and_remove_ads | isRegisted\(\)Z |
  pay_to_unlock_all_plans | has_buy_pro |
  isActiveSubscription\(\)Z | IS_SUBSCRIBED |
  IS_REMOVED_AD_PURCHASED | subscribed |
  getSubscribeValueFromPref\(\)Z | PURCHASED_PRO_VERSION |
   SUB_DETAILS | hasPremium |
   isAdRemoved | myvip |
   setPremium | def_pr |
   isGovUser\(\)Z |
   pro_trial | premium_trial | vip_trial |
   pro_offer | premium_offer | vip_offer |
   donate | isdonate
)\b
━━━━━━━━━━━━━━━━━━━━━━
Unlocking Premium (maybe)
Search:
(invoke-.*;->.*(Premium.*|RemoveAds.*|Pro|Vip.*|Paid.*|Purchased.*|Subscri.*|gold.*|Gold.*|subscri.*|paid.*|purchase.*|premium.*|vip.*|IsSubscription.*|isSubscription.*|proVersion.*|ProVersion.*|isProVersion.*|IsProVersion.*)\(.*\)Z)

Replace:
#${GROUP1}
invoke-static {}, Lapk/tool/patcher/Premium;->Premium()Z
#NIGHTZNERO



Search:
(const-string [pv]\d+, (\".*Premium.*|\".*IsPro.*|\".*RemoveAds.*|\".*Free.*|\"pro\"|\"Pro\"|\".*Vip.*\"|\".*Paid.*\"|\".*Purchase.*\"|\".*Subscri.*|\".*gold.*\"|\".*Ads.*|\".*Gold.*\"|\".*subscri.*|\".*paid.*|\".*purchase.*\"|\".*premium.*\"|\".*vip.*\"))\n\n    (const/4 ([pv]\d+), .*)\n\n    (invoke-interface \{([pv]\d+), ([pv]\d+), ([pv]\d+)\}, .*;->getBoolean\(Ljava/lang/String;Z\)Z)\n\n    (move-result ([pv]\d+))
Replace:
${GROUP1}
   ${GROUP3}
#    ${GROUP5}
#    ${GROUP9}
const/4 ${GROUP10}, 0x1
#NIGHTZNERO



Search:
([ias]get-boolean ([pv]\d+).*;->.*(Premium.*|RemoveAds.*|Pro|Vip.*|Paid.*|Purchased.*|Subscri.*|gold.*|Gold.*|subscri.*|paid.*|purchase.*|premium.*|vip.*|proVersion.*|ProVersion.*):Z)
Replace:
#${GROUP1}
const/4 ${GROUP2}, 0x1
#NIGHTZNERO
━━━━━━━━━━━━━━━━━━━━━━
