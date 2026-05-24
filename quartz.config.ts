import { QuartzConfig } from "./quartz/quartz/cfg"
import * as Plugin from "./quartz/quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "AIX Sovereign Stack",
    pageTitleSuffix: " · AIX KB",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "axiomid-knowledge-base.vercel.app",
    ignorePatterns: ["private", "templates", ".obsidian", "node_modules"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Space Grotesk",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#f8f9fa",
          lightgray: "#dee2e6",
          gray: "#868e96",
          darkgray: "#495057",
          dark: "#212529",
          secondary: "#00d4ff",
          tertiary: "#00ff41",
          highlight: "rgba(0, 212, 255, 0.12)",
          textHighlight: "#00ff4188",
        },
        darkMode: {
          light: "#0a0a0a",
          lightgray: "#1a1a2e",
          gray: "#4a4a6a",
          darkgray: "#c0c0d0",
          dark: "#e0e0f0",
          secondary: "#00d4ff",
          tertiary: "#00ff41",
          highlight: "rgba(0, 212, 255, 0.10)",
          textHighlight: "#00ff4188",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
