import { NextRequest, NextResponse } from "next/server";
import { askVoxeldev } from "@/lib/ai";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const message = body?.message;

    if (typeof message !== "string" || !message.trim()) {
      return NextResponse.json(
        { error: "Message is required." },
        { status: 400 }
      );
    }

    const response = await askVoxeldev(message);

    return NextResponse.json({
      response
    });
  } catch (error) {
    console.error("voxeldev chat error:", error);

    return NextResponse.json(
      { error: "Failed to generate a response." },
      { status: 500 }
    );
  }
}
