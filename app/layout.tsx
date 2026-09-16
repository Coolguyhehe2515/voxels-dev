import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "voxeldev",
  description: "AI-powered development workspace"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
