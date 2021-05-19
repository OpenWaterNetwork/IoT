export default {
  "title": "OpenWaterNetwork",
  "tagline": "Promoting Open Source and Open Access data for Water Resource Management",
  "url": "https://fabianastudillo.github.io",
  "baseUrl": "/IoT/es/",
  "onBrokenLinks": "throw",
  "onBrokenMarkdownLinks": "warn",
  "favicon": "img/favicon.ico",
  "organizationName": "OpenWaterNetwork",
  "projectName": "IoT",
  "i18n": {
    "defaultLocale": "en",
    "locales": [
      "en",
      "es"
    ],
    "localeConfigs": {}
  },
  "themeConfig": {
    "navbar": {
      "title": "OpenWaterNetwork",
      "logo": {
        "alt": "OpenWaterNetwork",
        "src": "img/logo.svg"
      },
      "items": [
        {
          "type": "localeDropdown",
          "position": "left",
          "dropdownItemsBefore": [],
          "dropdownItemsAfter": []
        },
        {
          "type": "doc",
          "docId": "intro",
          "position": "left",
          "label": "Tutorial",
          "activeSidebarClassName": "navbar__link--active"
        },
        {
          "href": "https://github.com/facebook/docusaurus",
          "label": "GitHub",
          "position": "right"
        }
      ],
      "hideOnScroll": false
    },
    "footer": {
      "style": "dark",
      "links": [
        {
          "title": "Docs",
          "items": [
            {
              "label": "Tutorial",
              "to": "/docs/intro"
            }
          ]
        },
        {
          "title": "Community",
          "items": [
            {
              "label": "Twitter",
              "href": "https://twitter.com/openwaternetwork"
            }
          ]
        },
        {
          "title": "More",
          "items": [
            {
              "label": "Blog",
              "to": "/blog"
            },
            {
              "label": "GitHub",
              "href": "https://github.com/OpenWaterNetwork/IoT"
            }
          ]
        }
      ],
      "copyright": "Copyright © 2021 Open Water Network."
    },
    "colorMode": {
      "defaultMode": "light",
      "disableSwitch": false,
      "respectPrefersColorScheme": false,
      "switchConfig": {
        "darkIcon": "🌜",
        "darkIconStyle": {},
        "lightIcon": "🌞",
        "lightIconStyle": {}
      }
    },
    "docs": {
      "versionPersistence": "localStorage"
    },
    "metadatas": [],
    "prism": {
      "additionalLanguages": []
    },
    "hideableSidebar": false
  },
  "presets": [
    [
      "@docusaurus/preset-classic",
      {
        "docs": {
          "sidebarPath": "/home/fabian/MEGA/DEET/ProyectoIoD/IoT/sidebars.js",
          "editUrl": "https://github.com/OpenWaterNetwork/IoT/blob/documentation/"
        },
        "blog": {
          "showReadingTime": true,
          "editUrl": "https://github.com/OpenWaterNetwork/IoT/blob/documentation/blog/"
        },
        "theme": {
          "customCss": "/home/fabian/MEGA/DEET/ProyectoIoD/IoT/src/css/custom.css"
        }
      }
    ]
  ],
  "baseUrlIssueBanner": true,
  "onDuplicateRoutes": "warn",
  "customFields": {},
  "plugins": [],
  "themes": [],
  "titleDelimiter": "|",
  "noIndex": false
};